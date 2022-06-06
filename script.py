import requests
from base64 import b64encode
from nacl import encoding, public
import json
import csv

baseurl = "https://api.github.com" # Don't change this line
secrets_csv_file = "secrets.csv" #you can change the name of csv file but make sure it is in the same directory as this script with the same name

owner =  "owner-name"
repos =  ["repo-1","repo-2"]  

email = "your-login-email@domain.com" # Enter your email here
personal_access_token = "" #read readme.md file to know how to get this token
auth_token = 'Basic ' + b64encode(bytes(email + ':' + personal_access_token, 'utf-8')).decode('ascii')

headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': auth_token,
    }

def check_token_access():
    url = baseurl + "/" + "user"
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    return (response.status_code == 200)

def get_secret(owner, repo,secret_name):
    url = baseurl + "/repos/"+owner+"/"+repo+"/actions/secrets/" + secret_name
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def get_public_key(owner, repo):
    url = baseurl + "/repos/"+owner+"/"+repo+"/actions/secrets/public-key" 
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def encrypt(public_key: str, secret_value: str) -> str:
  """Encrypt a Unicode string using the public key."""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")

def add_secret(owner, repo, secret_name, secret_value,key_id):
    url = baseurl + "/repos/"+owner+"/"+repo+"/actions/secrets/" + secret_name
    payload = {"encrypted_value":secret_value,"key_id":key_id}
    payload= json.dumps(payload)
    headers['Content-Type']= 'application/x-www-form-urlencoded'
    response = requests.request("PUT", url, headers=headers, data=payload)
    return(response.status_code, response.text)

def main():
    if not check_token_access():
        print("Invalid token")
        exit(1)
    for repo in repos:
        public_key = get_public_key(owner, repo)
        print("Fetched Public Key to Encrypt Secret")
        with open(secrets_csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                secret_name = row[0]
                secret_value = row[1]
                secret_value = encrypt(public_key['key'], secret_value)
                print("Pushing Secret: ", secret_name)
                result = add_secret(owner, repo, secret_name, secret_value,public_key['key_id'])
                if result[0] == 201:
                    print("Added Secret: ", secret_name)
                elif result[0] == 204:
                    print("Updating Secret : ", secret_name)
                else:
                    print("Error while adding Secret : ", secret_name)
                    print(result[0],result[1])
main()
# check_token_access()
# Create GitHub Secrets using Python

Using this python script you create bulk secrets in multiple repos at once programmatically with ease.

### Pre-requisites
1. Python v3.5 or above installed in your System
2. Python IDE or VS Code (for editing the script)
3. GitHub Account along with repo details
4. GitHub Personal Access Token

### Generate a GitHub Personal Access Token 

If you're trying to use this application, we'll need to generate a GitHub Personal Access Token (similar to OAuth token) to use this application.

> If you have existing un-expired personal token already. You can skip this step 

1. Visit [https://github.com/settings/tokens](https://github.com/settings/tokens) after you login into your GitHub account.

2. Click **Generate new token** and choose following scopes

        Note: (Enter any usual name)
        Scopes:
            [X] repo
                [X] repo:status
                [X] repo_deployment
                [X] public_repo
                [X] repo:invite
                [X] security_events
            [X] workflow

3. Click **Generate token**.

4. Copy the generated string to a safe place, such as a password safe. 

### Other required things
1. Your login Email ID
2. Owner of Repos
3. List of Repos
4. List of Secrets to be added along with values [keep dummy values if you want to add empty secret which will be added later] as csv file

##### How to find owner name ?

For any github URL the URL is formatted is as below

https://github.com/<**Owner Name**>/<**Repository Name**>

for this current repo the URL will be as follows

https://github.com/Upendra-Thunuguntla/create-bulk-github-secrets

here 

**Owner** = Upendra-Thunuguntla

**Repo** = create-bulk-github-secrets

## Configuring the Script with above requirments

Clone or download this repo and edit the ```script.py``` with above fetched values as shown below

> This script only supports multiple repositories which are under single owner. If there are multiple owners you need to run this script for each owner and their repos seperatley  

    owner =  ""
    repos =  [""]
    email = ""
    personal_access_token = ""
    
This program will automatically validate the access token and create all given secrets in mentioned repos in list.




> This Tool is made to be as simple and useful as possible. Hope you like it and find it useful


##  Modules Required
In order to Run this python script you need these modules in your system.
As an Admin/Root user on your system do:

    >> pip install requests
    >> pip install PyNaCl


## References Used
    >> https://docs.github.com/en/rest/repos/repos#get-a-repository
    >> https://docs.github.com/en/rest/actions/secrets#get-an-environment-public-key
    >> https://docs.github.com/en/rest/actions/secrets#create-or-update-an-environment-secret
    >> https://docs.github.com/en/rest/actions/secrets#get-a-repository-public-key
    >> https://docs.github.com/en/rest/actions/secrets#create-or-update-a-repository-secret
    >> https://docs.github.com/en/rest/actions/secrets#get-a-repository-secret
    
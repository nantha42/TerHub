import requests 
import json
import jwt
import sys 
import getopt


def create_repository(name,private=False):
    
    response = requests.post(
        url=f"https://api.github.com/user/repos",
        headers={
            # "User":user,
            "Authorization":f"token {access_token}",
            "Accept": "application/vnd.github.v3+json"
        },
        data=json.dumps({'name':name,'private':private})
    )
    if response.status_code == 201:
        out = json.loads(response.text)
        file = open("out.json","w")
        json.dump(out,file)
        file.close()
        print("Created Successfully")
        print("URL: ",out["clone_url"])
    else:
        print(response.status_code)
        print(response.text)

def delete_repository(name,user):
    response = requests.delete(
        url =f"https://api.github.com/repos/{user}/{name}",
        headers={
            "Authorization":f"token {access_token}",
            "Accept": "application/vnd.github.v3+json"
        },
        data = json.dumps({'name':name})
    )
    if 200< response.status_code <210:
        print(response.status_code)
        print(f"Deleted repository {name} successfully")
    else:
        print(response.status_code)
        print(response.text)


    
if __name__ == '__main__':
    access_token = None
    user = None 
    with open("tokens.dat","r") as file:
        access_token = file.read().split("\n")[-1]
    with open("users.dat","r") as file:
        user = file.read().split("\n")[-1]
    
    arguments = len(sys.argv)
    
    opt,rem = getopt.getopt(sys.argv[1:],"cd",["name =","private =","hel="])
    name = None
    private = None
    option = None
    for i,v in opt:
        if i=="--name ":
            name = v
        elif i == "--private ":
            if v == 'false':
                private = False
            elif v == 'true':
                private = True 
            else:
                private = False
        elif i=='-c':
            option = "create"
        elif i=='-d':
            option = "delete"

    # print("Name: ",name)
    # print("Private: ",private)
    # print(f"Option: {option}")
    
    if option == "create":
        if name != None:
            create_repository(name,private)

    elif option == "delete":
        if name!=None:
            delete_repository(name,user)

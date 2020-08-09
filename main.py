import requests 
import json
import jwt
import sys 
import getopt


access_token = "1f003ae8e8b2210d72630e6f3150b921a522a868"
user = "nantha42"

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
        print("URL: ",out["clone_url"])
    else:
        print(response.status_code)
        print(response.text)
    
if __name__ == '__main__':
    arguments = len(sys.argv)
    # opt,rem = getopt.getopt(['-aval'],'a:')
    opt,rem = getopt.getopt(sys.argv[1:],"",["name =","private =","hel="])
    name = None
    private = False
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
    print("Name: ",name)
    print("Private: ",private)
    create_repository(name,private)
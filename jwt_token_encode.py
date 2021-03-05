import os
import jwt
import time

from dotenv import load_dotenv


# - Enter the required data into an .env file in the same directory
# - Place the AuthKey you downloaded from your Apple Developer account
#   into the same directory
# - Adjust the expiry date
# - Run script
#
# ToDo
# - Error handling (file not found, filename wrong)


# Load Origin and Team_Id from .env table
load_dotenv()
ORIGIN = os.getenv("ORIGIN") #The SERVER_IP_ADDRESS that requests the map 
TEAM_ID = os.getenv("TEAM_ID") #Your Apple Developer Team Id

# Adjust expiry date
EXPIRY = 365 # Expiry in days

# File from Apple: AuthKey_{KEY ID}.p8
files = os.listdir(os.curdir)
for file in files:
    if file.endswith(".p8"):
        filename = file
        if file.startswith("AuthKey_"):
            key_id = filename[8:-3]
        break

# Get the content of the .py file
with open(filename) as f:
    content_p8 = f.read()

# prepare payload
payload = {
    "iss" : TEAM_ID,
    "iat" : str(round(time.time())),
    "exp" : str(round(time.time()) + EXPIRY * 86400),
    "origin" : ORIGIN
}

# prepare hader
header = {
    "kid" : key_id,
    "typ" : 'JWT',
    "alg" : 'ES256'
}


jwt_auth_token = jwt.encode(payload, content_p8, 'ES256', headers = header)

# Use your jwt_aut_token
print(jwt_auth_token)

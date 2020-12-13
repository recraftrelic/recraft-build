from dotenv import load_dotenv

import os

load_dotenv()

token = os.getenv("TOKEN")
main_domain = os.getenv("MAIN_DOMAIN")
apiEndPoint = "https://api.digitalocean.com/v2"

headers = {
    'content-type': "application/json",
    'Authorization': "Bearer " + token
}

#The requests module should be installed in your system before running this program
#It fetches and prints out hello.py on github
#Date: 22/12/2024

import requests

raw_url = "https://raw.githubusercontent.com/loachana/COE3200_01_Intro/refs/heads/main/hello.py"

response = requests.get(raw_url)

if response.status_code == 200:
    # Save the script locally or execute it
    with open("fetched_script.py", "w") as file:
        file.write(response.text)
    print("Script fetched and saved as 'fetched_script.py'")
    print("-----------------------------------------------")
    print(response.text)
else:
    print(f"Failed to fetch the script. HTTP Status Code: {response.status_code}")

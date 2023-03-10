import argparse
import json
import requests

# Banner
print("")
print("      .~~~~`\~~\        ")   
print("     ;       ~~ \       ")
print("     |           ;      ")
print(" ,--------,______|---.  ")
print("/          \-----`    \ ")
print("`.__________`-_______-' ")
print(" O S I N T  x  C U R P  ")
print("")

def get_config():
    try:
        with open("config.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_args():
    parser = argparse.ArgumentParser(description="Retrieve data from Mexico's CURP RENAPO API")
    parser.add_argument("curp", type=str, help="The CURP to retrieve")
    return parser.parse_args()

def main():
    config = get_config()
    args = get_args()

    curp = args.curp
    endpoint = "/v1/curp"
    url = "https://curp-renapo.p.rapidapi.com" + endpoint
    api_key = config.get("X-RapidAPI-Key")

    if api_key is None:
        print("Error: No API key specified.")
        return

    headers = {
        "X-RapidAPI-Host": "curp-renapo.p.rapidapi.com",
        "X-RapidAPI-Key": api_key
    }

    response = requests.get(f"{url}/{curp}", headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Do something with the data
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}.")

if __name__ == "__main__":
    main()

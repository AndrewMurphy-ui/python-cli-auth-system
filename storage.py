import json


def load_cli():

    try:
        with open("users.json", "r", encoding="utf-8") as file:
            return json.load(file)


    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("error, the file type and is not json format!")
        return None



def save_cli(users):
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)





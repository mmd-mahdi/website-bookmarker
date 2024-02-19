import webbrowser
import clipboard
import json


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}


def save_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def add_website(website, url, data):
    data["websites"][website] = url
    return data


data = load_data("./data.json")

print("hi what website do you looking for?")
inp = input()
while len(inp):
    if inp in data["websites"]:
        print("Great! I got the URL! Choose one of this two option "
              "1.Copy to clipborad"
              "2.Open website")
        index = int(input())
        if index == 1:
            clipboard.copy(data["websites"][inp])
            print("test 1 checked")
        elif index == 2:
            webbrowser.open(data["websites"][inp], new=0, autoraise=True)
        else:
            print("unknown input")
    else:
        print("i dont have this website pls add url")
        data = add_website(inp,input(),data)
        save_data(data,"./data.json")

    inp = input()

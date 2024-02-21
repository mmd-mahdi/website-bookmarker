import json
import clipboard
import webbrowser


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


def copyToClipboard(data, website):
    clipboard.copy(data["websites"][website])


def openBrowser(data, website):
    webbrowser.open(data["websites"][website], new=0, autoraise=True)


def menu():
    print("Great!! we have this website!")
    print("choose what do you want: ")
    print("1)copy to clipboard")
    print("2)open webpage")
    return int(input())


def book_marker(file_name):
    data = load_data(file_name)
    while True:
        user_input = input("what are you looking for?")
        if user_input in data["websites"]:
            menuChoose = menu()
            if menuChoose == 1:
                copyToClipboard(data, user_input)
            elif menuChoose == 2:
                openBrowser(data, user_input)
            else:
                print("bad request")
        else:
            print(f"sorry but there is no website such{user_input} do you want to add it or type out for exit")
            temp = input()
            if temp != "out":
                data = add_website(user_input, temp, data)
                save_data(data, file_name)

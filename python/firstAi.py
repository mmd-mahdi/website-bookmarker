import webbrowser
import clipboard
import json

with open("data.json") as database:
  temp = database.read()


data = json.loads(temp)
print("hi what website do you looking for?")
inp = input()
while len(inp):
  if inp in data:
    print("Great! I got the URL! Choose one of this two option "
          "1.Copy to clipborad"
          "2.Open website")
    index = int(input())
    if index == 1:
      clipboard.copy(data[inp])
      print("test 1 checked")
    elif index == 2:
      webbrowser.open(data[inp], new=0, autoraise=True)
    else:
      print("unknown input")
  else:
    print("i dont have this website pls add url")
    data[inp] = input()
    # database.write(data[inp])
    print("thans for adding some info")
  inp = input()




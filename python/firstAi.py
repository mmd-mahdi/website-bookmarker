import webbrowser
import clipboard

websites = {"google":'https://www.google.com'}
print("hi what website do you looking for?")
inp = input()
while len(inp) :
  if inp in websites:
    print("Great! I got the URL! Choose one of this two option "
          "1.Copy to clipborad"
          "2.Open website")
    index = int(input())
    if index == 1:
      clipboard.copy(websites[inp])
    elif index == 2:
      webbrowser.open(websites[inp], new=0, autoraise=True)
    else:
      print("unknown input")
  else:
    print("i dont have this website pls add url")
    websites[inp] = input()  
    print("thans for adding some info")
  inp = input()




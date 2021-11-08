
import webbrowser as web

def checknum(number, errorText):
    try:
        print("You wrote " + str(int(number)))
    except:
        print(errorText)

def opensite(site, errorText):
    try:
        web.open(site)
    except:
        print(errorText)

def cucumber(idk): #idk why i added this function
    if idk == "iateit":
        print("was it yummy?")
    else:
        print("cucumber is yummy")
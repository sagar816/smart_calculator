responses=["Welcome to smart calculator","Hi, My name is alexa","Thanks",
           "Sorry, this is beyond my ability"]

def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def end():
    print(responses[2])
    input("Press enter key to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])

operations={"PLUS": add, "ADDITION":add, "ADD": add, "SUM":add, "MINUS":sub, "SUBTRACTION":sub, "SUBTRACT":sub,
            "DIFFRENCE":sub, "PRODUCT":multiply, "MULTIPLICATION":multiply, "DIVIDE":division, "DIVISION":division}
commands={"NAME":myname, "END":add, "EXIT":end, "CLOSE":end}


    

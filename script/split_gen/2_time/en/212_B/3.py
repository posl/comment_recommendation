def main():
    x = input()
    if x[0] == x[1] == x[2] == x[3]:
        print("Weak")
    elif x[0] == "9" and x[1] == "0" and x[2] == "1" and x[3] == "2":
        print("Weak")
    elif x[0] == str(int(x[1])-1) and x[1] == str(int(x[2])-1) and x[2] == str(int(x[3])-1):
        print("Weak")
    else:
        print("Strong")

def main():
    s = input()
    s = s.replace("()", "")
    while s != s.replace("()", ""):
        s = s.replace("()", "")
    if s == "":
        print("Yes")
    else:
        print("No")

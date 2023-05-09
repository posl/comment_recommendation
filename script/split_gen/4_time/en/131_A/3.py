def main():
    str = input()
    if str[0] == str[1] and str[1] == str[2]:
        print("Bad")
    elif str[1] == str[2] and str[2] == str[3]:
        print("Bad")
    else:
        print("Good")

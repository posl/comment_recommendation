def main():
    s = input()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print("Bad")
            return
    print("Good")

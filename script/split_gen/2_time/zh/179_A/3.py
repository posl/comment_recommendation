def main():
    s = input()
    if s[len(s)-1] == "s":
        print(s + "es")
    else:
        print(s + "s")

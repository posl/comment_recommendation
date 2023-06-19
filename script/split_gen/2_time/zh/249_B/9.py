def main():
    s = input()
    if len(s) < 2 or len(s) > 100:
        print("No")
    elif s.lower() == s or s.upper() == s:
        print("No")
    elif s.isalnum():
        print("Yes")
    else:
        print("No")

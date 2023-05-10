def main():
    s = input()
    if (s.islower() or s.isupper() or len(set(s)) != len(s)):
        print("No")
    else:
        print("Yes")

def main():
    s = input()
    if s.islower() or s.isupper() or len(s) != len(set(s)):
        print("No")
    else:
        print("Yes")

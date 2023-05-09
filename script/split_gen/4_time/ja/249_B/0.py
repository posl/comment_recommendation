def main():
    s = input()
    if len(s) == len(set(s)) and any(c.islower() for c in s) and any(c.isupper() for c in s):
        print("Yes")
    else:
        print("No")

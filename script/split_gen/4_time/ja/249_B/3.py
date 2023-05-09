def main():
    s = input()
    if len(s) != len(set(s)):
        print("No")
    else:
        print("Yes")

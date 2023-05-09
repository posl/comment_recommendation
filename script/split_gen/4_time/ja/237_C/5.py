def main():
    s = input()
    n = len(s)
    if s == s[::-1]:
        if n%2 == 0:
            print("Yes")
        else:
            print("No")
    else:
        if n%2 == 0:
            print("No")
        else:
            print("Yes")

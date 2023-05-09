def main():
    n = int(input())
    s = input()
    if n % 2 == 0:
        if s[0:n//2] == s[n//2:]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

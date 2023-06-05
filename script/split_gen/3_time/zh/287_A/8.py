def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] == "For":
            s[i] = 1
        else:
            s[i] = 0
    if sum(s) > n//2:
        print("Yes")
    else:
        print("No")

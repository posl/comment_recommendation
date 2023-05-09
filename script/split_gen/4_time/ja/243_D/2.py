def main():
    n,x = map(int,input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == "U":
            ans //= 2
        elif s[i] == "L":
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    print(ans)

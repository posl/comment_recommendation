def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ans = 1
    for i in range(n-1):
        if s[i] == "OR":
            ans += 2**(i+1)
    print(ans)

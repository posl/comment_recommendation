def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    ans = 0
    for i in range(n):
        ans += 10
        for j in range(10):
            if s[i] == s[(i+j)%n]:
                ans -= j
                break
    print(ans)

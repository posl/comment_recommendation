def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(10):
        for j in range(n):
            if s[j][i] == '0':
                s[j] = s[j][1:]
                break
        else:
            for j in range(n):
                s[j] = s[j][1:]
            ans += 1
    print(ans)

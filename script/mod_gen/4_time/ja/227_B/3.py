def problems227_b():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                ans = ans + 1
    print(ans)

if __name__ == '__main__':
    problems227_b()
def problems280_a():
    h,w = map(int,input().split())
    ans = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                ans += 1
    print(ans)

if __name__ == '__main__':
    problems280_a()
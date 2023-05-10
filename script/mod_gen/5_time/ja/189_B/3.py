def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for _ in range(n):
        vi, pi = map(int, input().split())
        v.append(vi)
        p.append(pi)
    ans = -1
    alc = 0
    for i in range(n):
        alc += v[i] * p[i]
        if alc > x * 100:
            ans = i+1
            break
    print(ans)

if __name__ == '__main__':
    main()
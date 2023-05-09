def main():
    n, x = map(int, input().split())
    v = [0] * n
    p = [0] * n
    for i in range(n):
        v[i], p[i] = map(int, input().split())
    ans = -1
    alc = 0
    for i in range(n):
        alc += v[i] * p[i]
        if alc > x * 100:
            ans = i + 1
            break
    print(ans)

if __name__ == '__main__':
    main()
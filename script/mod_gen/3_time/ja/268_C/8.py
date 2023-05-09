def main():
    n = int(input())
    p = list(map(int, input().split()))
    d = [0] * n
    for i, v in enumerate(p):
        d[v] = i
    res = 0
    for i in range(n):
        if d[i] == i:
            res += 1
    print(res)

if __name__ == '__main__':
    main()
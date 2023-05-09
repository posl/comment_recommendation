def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    xk = [map(int, input().split()) for _ in range(q)]
    x, k = [list(i) for i in zip(*xk)]
    for i in range(q):
        cnt = 0
        for j in range(n):
            if a[j] == x[i]:
                cnt += 1
                if cnt == k[i]:
                    print(j + 1)
                    break
        else:
            print(-1)
main()

if __name__ == '__main__':
    main()
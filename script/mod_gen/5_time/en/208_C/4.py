def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = [k // n] * n
    k = k % n
    for i in range(k):
        res[i] += 1
    for i in range(n):
        print(res[i])

if __name__ == '__main__':
    main()
def main():
    n, k = map(int, input().split())
    snuke = [0] * n
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for j in range(d):
            snuke[a[j] - 1] += 1
    cnt = 0
    for i in range(n):
        if snuke[i] == 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
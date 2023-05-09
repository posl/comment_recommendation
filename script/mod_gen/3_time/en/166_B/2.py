def main():
    N, K = map(int, input().split())
    d = [0] * K
    for i in range(K):
        d[i] = int(input())
    a = [0] * K
    for i in range(K):
        a[i] = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(K):
            if i+1 in a[j]:
                break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
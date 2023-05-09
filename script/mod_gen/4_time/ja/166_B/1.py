def main():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        if i+1 not in sum(A, []):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
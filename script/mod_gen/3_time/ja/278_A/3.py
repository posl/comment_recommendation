def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(K):
        A.pop(0)
        A.append(0)
    print(*A)

if __name__ == '__main__':
    main()
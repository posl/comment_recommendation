def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(A.pop(0))
        A.append(0)
    A.pop()
    print(' '.join(map(str, A)))

if __name__ == '__main__':
    main()
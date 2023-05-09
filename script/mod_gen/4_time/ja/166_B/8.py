def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    A = [item for sublist in A for item in sublist]
    A = list(set(A))
    print(N - len(A))

if __name__ == '__main__':
    main()
def main():
    A, B, C, K = map(int, input().split())
    if (A >= K):
        print(K)
        return
    elif (A + B >= K):
        print(A)
        return
    else:
        print(A - (K - A - B))

if __name__ == '__main__':
    main()
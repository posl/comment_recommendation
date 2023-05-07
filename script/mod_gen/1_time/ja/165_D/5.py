def main():
    A, B, N = map(int, input().split())
    if B <= N:
        X = B-1
    else:
        X = N
    print((A*X)//B - A*(X//B))

if __name__ == '__main__':
    main()
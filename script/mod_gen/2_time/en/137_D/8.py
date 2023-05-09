def main():
    N, M = map(int, input().split())
    B = []
    for i in range(N):
        A, B = map(int, input().split())
        B.append((A, B))
    B.sort(key=lambda x: x[0])
    print(B)

if __name__ == '__main__':
    main()
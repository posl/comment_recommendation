def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(1, N+1):
        B.append(sum(A[:i]))
    print(max(max(B), 0))

if __name__ == '__main__':
    main()
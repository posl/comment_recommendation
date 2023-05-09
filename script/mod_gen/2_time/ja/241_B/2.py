def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(M):
        if B[i] not in A:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()
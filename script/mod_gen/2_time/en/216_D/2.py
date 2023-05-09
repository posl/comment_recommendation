def main():
    N, M = map(int, input().split())
    k = [0] * M
    a = [0] * M
    for i in range(M):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    print('Yes')

if __name__ == '__main__':
    main()
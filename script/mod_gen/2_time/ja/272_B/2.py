def main():
    N, M = map(int, input().split())
    all = set()
    for i in range(M):
        k = list(map(int, input().split()))
        k.pop(0)
        all.update(k)
    if len(all) == N:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
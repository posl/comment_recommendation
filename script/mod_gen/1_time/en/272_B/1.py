def main():
    N, M = map(int, input().split())
    x = []
    for _ in range(M):
        x.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(N):
            if i != j:
                if not (i+1 in x[j]):
                    print('No')
                    return
    print('Yes')
    return

if __name__ == '__main__':
    main()
def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    for i in range(N):
        if K >= AB[i][0]:
            K += AB[i][1]
        else:
            break
    print(K)

if __name__ == '__main__':
    main()
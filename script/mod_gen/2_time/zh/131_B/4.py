def main():
    N, L = map(int, input().split())
    sum = 0
    for i in range(N):
        sum += L+i
    if L >= 0:
        sum -= L
    elif L+N-1 < 0:
        sum -= L+N-1
    print(sum)

if __name__ == '__main__':
    main()
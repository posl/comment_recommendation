def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if S[i] % 2 == 0:
            if S[i] % 4 != 0:
                count += 1
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
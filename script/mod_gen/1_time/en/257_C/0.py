def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if S[i] == '0':
            if W[i] < 50:
                count += 1
        else:
            if W[i] >= 50:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
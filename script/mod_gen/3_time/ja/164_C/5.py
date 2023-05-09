def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        else:
            if S[i-1] != S[i]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
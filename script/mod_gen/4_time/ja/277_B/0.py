def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i] == S[i+1]:
            print('No')
            break
        elif i == N-2:
            print('Yes')
main()

if __name__ == '__main__':
    main()
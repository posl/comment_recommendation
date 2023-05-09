def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print('Yes' if len(set(S)) == N else 'No')

if __name__ == '__main__':
    main()
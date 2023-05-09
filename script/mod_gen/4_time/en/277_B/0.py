def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    if len(set(S)) == N:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
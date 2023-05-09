def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_set = set(S)
    if len(S) == len(S_set):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
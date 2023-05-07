def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 1:
        if len(set(A)) == N:
            print('No')
        else:
            print('Yes')
    elif N == 2:
        print('Yes')
    else:
        if max(A) - min(A) <= K:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
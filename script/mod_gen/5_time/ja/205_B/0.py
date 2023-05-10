def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [i for i in range(1, N+1)]
    B.sort()
    if A == B:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
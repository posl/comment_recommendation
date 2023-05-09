def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, N + 1):
        if i != A[i - 1]:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    main()
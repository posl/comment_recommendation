def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(set(A)) == N:
        print('YES')
    else:
        print('NO')
main()

if __name__ == '__main__':
    main()
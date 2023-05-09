def main():
    N, S, D = map(int, input().split())
    for _ in range(N):
        if S < int(input().split()[0]) and int(input().split()[1]) > D:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()
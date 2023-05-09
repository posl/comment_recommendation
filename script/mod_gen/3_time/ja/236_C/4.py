def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    set_T = set(T)
    for s in S:
        if s in set_T:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    S_set = set(S)
    T_set = set(T)
    if S_set & T_set:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
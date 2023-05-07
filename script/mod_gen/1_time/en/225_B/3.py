def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    if N == 3:
        print('Yes')
    else:
        if a.count(1) == 1:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
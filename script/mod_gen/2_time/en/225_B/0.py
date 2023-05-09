def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    if len(set(a)) == 1 and len(set(b)) == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
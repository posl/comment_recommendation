def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    if a.count(a[0]) == N-1:
        print('Yes')
    elif b.count(b[0]) == N-1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
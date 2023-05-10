def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # print(a)
    # print(b)
    sum = 0
    for i in range(N):
        if a[i] <= X and b[i] >= X:
            sum = sum + 1
    if sum == 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
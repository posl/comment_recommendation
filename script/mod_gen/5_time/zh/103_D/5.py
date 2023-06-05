def main():
    N, M = [int(x) for x in input().split()]
    a = []
    b = []
    for i in range(M):
        a_i, b_i = [int(x) for x in input().split()]
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    print(min(a[0]-1, N-b[-1], b[0]-a[-1], N-a[0]))

if __name__ == '__main__':
    main()
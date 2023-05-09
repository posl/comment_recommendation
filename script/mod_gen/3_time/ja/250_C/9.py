def main():
    N, Q = map(int, input().split())
    a = [i for i in range(1, N+1)]
    for _ in range(Q):
        x = int(input())
        a_index = a.index(x)
        if a_index == N-1:
            a[a_index], a[a_index-1] = a[a_index-1], a[a_index]
        else:
            a[a_index], a[a_index+1] = a[a_index+1], a[a_index]
    print(*a)

if __name__ == '__main__':
    main()
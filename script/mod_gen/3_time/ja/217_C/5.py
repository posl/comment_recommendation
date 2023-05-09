def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    q = [0] * N
    for i in range(N):
        q[p[i]-1] = i+1
    print(*q)

if __name__ == '__main__':
    main()
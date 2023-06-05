def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    q = [0]*N
    for i in range(N):
        q[p[i]-1] = i+1
    for i in range(N):
        print(q[i], end=" ")
    print()

if __name__ == '__main__':
    main()
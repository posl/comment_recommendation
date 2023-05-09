def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        #print(x)
        #print(A)
        #print(A.index(x))
        #print(A.count(x))
        print(N - A.index(x))

if __name__ == '__main__':
    main()
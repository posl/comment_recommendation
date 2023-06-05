def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    #print(T)
    A = T[0]
    B = 0
    for i in range(1, N):
        if A < B:
            A += T[i]
        else:
            B += T[i]
    print(max(A, B))

if __name__ == '__main__':
    main()
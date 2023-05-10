def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort()
    A = [AB[i][0] for i in range(N-1)]
    B = [AB[i][1] for i in range(N-1)]
    #print("A", A)
    #print("B", B)
    #print("AB", AB)
    count = 0
    for i in range(N-1):
        if A[i] == 1:
            count += 1
    if count == N-1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
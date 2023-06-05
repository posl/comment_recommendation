def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    max_height = 0
    for i in range(N):
        if A[i] > max_height+1:
            print(-1)
            return
        elif A[i] == max_height+1:
            max_height += 1
    print(N-max_height)

if __name__ == '__main__':
    main()
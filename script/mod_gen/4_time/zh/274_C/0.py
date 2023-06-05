def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(2*N+1)
    for i in range(N):
        B[A[i]] = i+1
    #print(B)
    for i in range(1, 2*N+1):
        if i == 1:
            print(0)
        else:
            j = i
            count = 0
            while j != 1:
                j = B[j]
                count += 1
            print(count)
main()

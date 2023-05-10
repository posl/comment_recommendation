def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0]*(2**N+1)
    for i in range(len(A)):
        B[A[i]] = i+1
    #print(B)
    for i in range(1, 2**N+1):
        j = i
        c = 0
        while j > 0:
            j = j//2
            c += 1
        print(c-1)
main()

if __name__ == '__main__':
    main()
def main():
    #read the input
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #sort A and B
    A.sort()
    B.sort()
    #find the minimum time
    min_time = 10**9
    for i in range(N):
        min_time = min(min_time, max(A[i], B[N-1-i]))
    print(min_time)

if __name__ == '__main__':
    main()
def main():
    #Read input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    
    #Find the maximum value of Ai + 1
    max_value = 0
    for i in range(N - 1):
        max_value = max(max_value, A[i + 1] - A[i])
    
    #Find the minimum value of Ai + 1
    min_value = 10 ** 18
    for i in range(N - 1):
        min_value = min(min_value, A[i + 1] - A[i])
    
    #Find the minimum value of Ai + 1 that is greater than or equal to k
    for k in K:
        if k >= max_value:
            print(A[N - 1] + k - max_value)
        else:
            #Binary search
            left = 0
            right = N - 1
            while left < right:
                mid = (left + right) // 2
                if A[mid] + k >= A[mid + 1]:
                    left = mid + 1
                else:
                    right = mid
            print(A[left] + k)

if __name__ == '__main__':
    main()
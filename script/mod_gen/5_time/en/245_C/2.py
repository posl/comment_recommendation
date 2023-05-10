def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    diff = 0
    for i in range(N):
        diff += abs(A[i] - B[i])
    
    if diff > K:
        print("No")
    elif (diff - K) % 2 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
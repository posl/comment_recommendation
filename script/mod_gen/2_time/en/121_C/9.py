def main():
    # Get input
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    # Sort by price
    sort_idx = sorted(range(N), key=lambda k: A[k])
    A = [A[i] for i in sort_idx]
    B = [B[i] for i in sort_idx]
    
    # Find the minimum amount of money
    ans = 0
    for i in range(N):
        if M > B[i]:
            ans += A[i] * B[i]
            M -= B[i]
        else:
            ans += A[i] * M
            break
    
    # Output
    print(ans)

if __name__ == '__main__':
    main()
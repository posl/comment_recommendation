def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    for i in range(N):
        if i+1 in B:
            A[i] = 0
    if max(A) == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()
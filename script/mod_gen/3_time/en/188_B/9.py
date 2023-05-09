def main():
    #input
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    #calc
    ans = 0
    for i in range(N):
        ans += A[i]*B[i]
    
    #output
    if ans == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
def main():
    #input
    N = int(input())
    T, A = map(int,input().split())
    H = list(map(int,input().split()))
    #calc
    ans = 1
    for i in range(2,N+1):
        if abs(T - H[ans-1]*0.006 - A) > abs(T - H[i-1]*0.006 - A):
            ans = i
    #output
    print(ans)

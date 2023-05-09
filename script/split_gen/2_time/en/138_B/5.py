def main():
    #get input
    N = int(input())
    A = list(map(int, input().split()))
    
    #compute
    sum = 0
    for i in range(N):
        sum += 1 / A[i]
    ans = 1 / sum
    
    #print output
    print(ans)

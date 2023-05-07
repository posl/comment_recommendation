def main():
    #read input
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    #initialize satisfaction points
    sat = 0
    
    #loop over dishes
    for i in range(N):
        #add satisfaction points from eating the dish
        sat += B[A[i]-1]
        
        #if the dish is not the last one and the next dish is consecutive
        if i < N-1 and A[i]+1 == A[i+1]:
            #add satisfaction points from eating consecutive dishes
            sat += C[A[i]-1]
    
    #print satisfaction points
    print(sat)

def main():
    #input
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    #solve
    #sort by B
    sort = sorted(enumerate(B),key=lambda x:x[1])
    #print(sort)
    time = 0
    for i in range(N):
        time += A[sort[i][0]]
        if time > sort[i][1]:
            print('No')
            return
    print('Yes')

def main():
    N,x,y = map(int,input().split())
    A = list(map(int,input().split()))
    A.append(0)
    A.insert(0,0)
    for i in range(1,N+1):
        for j in range(i+1,N+2):
            if abs(A[i]-A[j])+abs(j-i)==abs(x-y):
                print('Yes')
                return
    print('No')

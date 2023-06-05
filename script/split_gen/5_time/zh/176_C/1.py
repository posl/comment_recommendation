def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.insert(0,0)
    A.append(0)
    s = 0
    for i in range(len(A)-1):
        s += abs(A[i+1]-A[i])
    for i in range(1,len(A)-1):
        print(s+abs(A[i-1]-A[i+1])-abs(A[i-1]-A[i])-abs(A[i]-A[i+1]))
main()

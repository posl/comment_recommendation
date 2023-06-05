def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(len(A))
    #print(len(B))
    #print(max(B))
    #print(max(A))
    #print(sum(A))
    if max(B) < sum(A):
        print('No')
    else:
        print('Yes')

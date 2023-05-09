def main():
    N = int(input())
    A = []
    for i in range(N):
        x,y,p = map(int,input().split())
        A.append((x,y,p))
    #print(A)
    B = []
    for i in range(N):
        for j in range(N):
            if i != j:
                x1,y1,p1 = A[i]
                x2,y2,p2 = A[j]
                d = abs(x1-x2)+abs(y1-y2)
                if d <= p1*p2:
                    B.append((i,j))
    #print(B)
    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                x1,y1,p1 = A[i]
                x2,y2,p2 = A[j]
                d = abs(x1-x2)+abs(y1-y2)
                if d <= p1*p2:
                    ans = max(ans,abs(p1-p2))
    print(ans)

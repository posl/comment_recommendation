def main():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(0)
    a.append(0)
    a.insert(0,0)
    for i in range(1,n+2):
        for j in range(i+1,n+2):
            if i == j:
                continue
            p = [0,0]
            q = [0,0]
            p[0] = i
            p[1] = a[i]
            q[0] = j
            q[1] = a[j]
            if p[0] == q[0]:
                continue
            dis1 = (p[0]-q[0])**2 + (p[1]-q[1])**2
            dis2 = (p[0]-x)**2 + (p[1]-y)**2
            dis3 = (q[0]-x)**2 + (q[1]-y)**2
            if dis1 == dis2 + dis3:
                print("Yes")
                exit()
    print("No")

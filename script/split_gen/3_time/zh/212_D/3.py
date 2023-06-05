def main():
    q=int(input())
    p=[]
    x=[]
    for i in range(q):
        p.append(input().split())
    for i in range(q):
        if p[i][0]=='1':
            x.append(int(p[i][1]))
        elif p[i][0]=='2':
            for j in range(len(x)):
                x[j]+=int(p[i][1])
        else:
            print(min(x))
            x.remove(min(x))
main()

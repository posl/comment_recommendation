def main():
    #print("请输入X和N")
    x,n = map(int,input().split())
    #print("请输入p1到pN")
    p = list(map(int,input().split()))
    p.append(x)
    p.sort()
    #print(p)
    for i in range(len(p)):
        if p[i] == x:
            print(p[i+1])
            break

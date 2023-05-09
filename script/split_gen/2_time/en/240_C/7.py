def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(0,n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    print(a)
    print(b)
    for i in range(0,n):
        if x >= a[i] and x <= b[i]:
            print("Yes")
            return
    print("No")
    return

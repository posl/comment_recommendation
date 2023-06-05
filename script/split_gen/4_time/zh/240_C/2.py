def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(n):
        if x == a[i] or x == b[i]:
            print("Yes")
            break
        elif x < a[i]:
            print("No")
            break
        else:
            x = x - a[i]
            x = x + b[i]
            if i == n-1:
                print("Yes")

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(n, x)
    #print(a)
    #print(b)
    for i in range(n):
        x -= a[i]
        if x < 0:
            print("No")
            return
        x += b[i]
        #print(x)
    print("Yes")
    return

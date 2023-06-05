def get_price(A,B):
    for i in range(A,B+1):
        a = int(i*0.08)
        b = int(i*0.1)
        if a == A and b == B:
            return i
    return -1
A,B = map(int,input().split())
print(get_price(A,B))

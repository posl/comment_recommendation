def S(n):
    a = n//100
    b = n//10%10
    c = n%10
    return a+b+c
a,b = map(int,input().split())
print(max(S(a),S(b)))

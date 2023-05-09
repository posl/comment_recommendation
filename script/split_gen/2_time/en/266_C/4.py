def is_convex(A,B,C,D):
    def cross_product(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    return cross_product(A,B,C)*cross_product(A,B,D) > 0 and \
           cross_product(B,C,D)*cross_product(B,C,A) > 0 and \
           cross_product(C,D,A)*cross_product(C,D,B) > 0 and \
           cross_product(D,A,B)*cross_product(D,A,C) > 0
A = map(int, raw_input().split())
B = map(int, raw_input().split())
C = map(int, raw_input().split())
D = map(int, raw_input().split())
print "Yes" if is_convex(A,B,C,D) else "No"

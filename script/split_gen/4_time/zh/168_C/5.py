def main():
    a,b,h,m = map(int,input().split())
    import math
    h_a = 30*h + m/2
    b_a = 6*m
    #print(h_a,b_a)
    #print(math.cos(math.radians(h_a)))
    #print(math.cos(math.radians(b_a)))
    print(math.sqrt(a**2+b**2-2*a*b*(math.cos(math.radians(h_a-b_a)))))

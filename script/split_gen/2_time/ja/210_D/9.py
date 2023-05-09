def main():
    import sys
    from functools import reduce
    from operator import mul
    from math import gcd
    def lcm_base(x, y):
        return (x * y) // gcd(x, y)
    def lcm(*numbers):
        return reduce(lcm_base, numbers, 1)
    def lcm_list(numbers):
        return reduce(lcm_base, numbers, 1)
    H, W, C = map(int, input().split())
    A = []
    A.append([0]*(W+1))
    for i in range(H):
        A.append([0]+list(map(int, input().split())))
    #print(A)
    #print(A[1][1])
    #print(A[2][3])
    #print(A[3][3])
    #print(A[1][1] + A[2][3] + C*abs(1-2)+abs(1-3))
    #print(A[1][1] + A[3][3] + C*abs(1-3)+abs(1-3))
    #print(A[2][3] + A[3][3] + C*abs(2-3)+abs(3-3))
    #print(A[1][1] + A[2][3] + C*abs(1-2)+abs(1-3))
    #print(A[1][1] + A[3][3] + C*abs(1-3)+abs(1-3))
    #print(A[2][3] + A[3][3] + C*abs(2-3)+abs(3-3))
    #print(A[1][1] + A[2][3] + C*abs(1-2)+abs(1-3))
    #print(A[1][1] + A[3][3] + C*abs(1-3)+abs(1-3))
    #print(A[2][3] + A[3][3] + C*abs(2-3)+abs(3-3))
    #print(A[1][1] + A[2][3] + C*abs(1-2)+abs(1-3))
    #print(A[1][1] + A[3][3] + C*abs(1-3)+abs(1

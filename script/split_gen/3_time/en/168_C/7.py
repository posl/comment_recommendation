def solve():
    A, B, H, M = map(int, input().split())
    theta = (H*60+M)/720*2*math.pi
    phi = M/60*2*math.pi
    print(math.sqrt(A**2+B**2-2*A*B*math.cos(theta-phi)))
import math
solve()

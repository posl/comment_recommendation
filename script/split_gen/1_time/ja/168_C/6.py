def solve():
    A,B,H,M=map(int,input().split())
    H_angle=30*H+M/2
    M_angle=6*M
    angle=abs(H_angle-M_angle)
    if angle > 180:
        angle=360-angle
    angle=angle/180*math.pi
    print(math.sqrt(A**2+B**2-2*A*B*math.cos(angle)))

def main():
    import math
    A,B,H,M=map(int,input().split())
    Hrad=math.radians(30*H+0.5*M)
    Mrad=math.radians(6*M)
    Hx=math.cos(Hrad)*A
    Hy=math.sin(Hrad)*A
    Mx=math.cos(Mrad)*B
    My=math.sin(Mrad)*B
    print(math.sqrt((Hx-Mx)**2+(Hy-My)**2))

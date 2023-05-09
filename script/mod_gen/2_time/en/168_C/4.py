def main():
    A,B,H,M=map(int,input().split())
    h=30*H+M/2
    m=6*M
    print(((A**2+B**2-2*A*B*math.cos(math.radians(abs(h-m))))**0.5))

if __name__ == '__main__':
    main()
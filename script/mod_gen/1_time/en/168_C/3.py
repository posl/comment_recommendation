def main():
    A,B,H,M = map(int,input().split())
    theta1 = 2*math.pi*(H/12+M/720)
    theta2 = 2*math.pi*(M/60)
    print(math.sqrt(A**2+B**2-2*A*B*math.cos(theta1-theta2)))

if __name__ == '__main__':
    main()
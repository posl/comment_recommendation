def main():
    import math
    A, B, H, M = map(int, input().split())
    ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(30*H+M/2)))
    print(ans)

if __name__ == '__main__':
    main()
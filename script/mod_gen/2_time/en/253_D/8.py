def main():
    N, A, B = map(int, input().split())
    lcm = A*B//math.gcd(A,B)
    ans = N//A + N//B - N//lcm
    print(ans)

if __name__ == '__main__':
    main()
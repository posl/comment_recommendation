def main():
    A,B,C,D = map(int,input().split())
    ans = B - A + 1
    ans -= B // C - (A - 1) // C
    ans -= B // D - (A - 1) // D
    ans += B // (C * D // gcd(C,D)) - (A - 1) // (C * D // gcd(C,D))
    print(ans)

if __name__ == '__main__':
    main()
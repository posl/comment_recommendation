def main():
    A, B, C, D = map(int, input().split())
    CD = C*D//math.gcd(C, D)
    print(B-A+1-(B//C+B//D-B//CD)-(A//C+A//D-A//CD-1))

if __name__ == '__main__':
    main()
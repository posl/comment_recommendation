def main():
    A, B, C, D = map(int, input().split())
    print((B-A+1) - B//C - B//D + B//lcm(C,D) + A//C + A//D - A//lcm(C,D) - (A-1)//C - (A-1)//D + (A-1)//lcm(C,D))

if __name__ == '__main__':
    main()
def main():
    A,B,C,D = map(int,input().split())
    ans = B - A + 1
    ans -= B//C - (A-1)//C
    ans -= B//D - (A-1)//D
    ans += B//lcm(C,D) - (A-1)//lcm(C,D)
    print(ans)

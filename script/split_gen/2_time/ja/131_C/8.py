def main():
    A,B,C,D = map(int,input().split())
    #print(A,B,C,D)
    ans = B - A + 1
    ans -= B // C - (A - 1) // C
    ans -= B // D - (A - 1) // D
    ans += B // (C * D) - (A - 1) // (C * D)
    print(ans)

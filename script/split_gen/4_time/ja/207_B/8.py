def main():
    A,B,C,D = map(int, input().split())
    if A <= B:
        print(-1)
        return
    if C >= D*B:
        print(0)
        return
    if C*B >= A:
        print(-1)
        return
    if C*B < A:
        if (A - C*B) % (B*(D-1)) == 0:
            print((A - C*B) // (B*(D-1)))
        else:
            print((A - C*B) // (B*(D-1)) + 1)
        return

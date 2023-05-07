def main():
    A, B = map(int, input().split())
    ans = 0
    if A <= B:
        ans = A
    else:
        ans = B + (A - B) / (2**(1/2))
    print(ans)

def main():
    # input
    a, b, c = map(int, input().split())
    # compute
    # output
    if a*a + b*b < c*c:
        print("Yes")
    else:
        print("No")

def main():
    # read input
    a, b, c = map(int, input().split())
    # solve
    result = max(a+b+c, a+b*c, a*b+c, a*b*c, (a+b)*c, a*(b+c))
    # output
    print(result)

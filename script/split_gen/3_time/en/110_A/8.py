def main():
    # read in the input
    a, b, c = map(int, input().split())
    # find the maximum possible amount of the allowance
    max_allowance = max(a+b+c, a*b*c, a*(b+c), (a+b)*c)
    # print the maximum possible amount of the allowance
    print(max_allowance)

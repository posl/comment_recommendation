def main():
    # read input
    a, b, c = input().split()
    # convert to int
    a = int(a)
    b = int(b)
    c = int(c)
    # find the max of the three
    if (a > b) and (a > c):
        max = a
    elif (b > a) and (b > c):
        max = b
    elif (c > a) and (c > b):
        max = c
    # find the min of the three
    if (a < b) and (a < c):
        min = a
    elif (b < a) and (b < c):
        min = b
    elif (c < a) and (c < b):
        min = c
    # print the sum of the other two
    print(a+b+c-max-min)
main()

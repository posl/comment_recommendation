def main():
    # get input
    a = list(map(int, input().split()))
    # set initial value
    k = 0
    # set counter
    count = 0
    # loop until counter reaches 3
    while count < 3:
        # set next value
        k = a[k]
        # increment counter
        count += 1
    # print result
    print(k)

def main():
    # get input
    k = int(input())
    # count the number of even and odd numbers
    even = k // 2
    odd = k - even
    # print the result
    print(even * odd)

def main():
    # A = regular price
    # B = discounted price
    A, B = [int(x) for x in input().split()]
    print(100 * (1 - B/A))
main()

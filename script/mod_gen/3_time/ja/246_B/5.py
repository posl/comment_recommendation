def main():
    A, B = map(int, input().split())
    # A, B = 246, 402
    # A, B = 1, 0
    # A, B = 3, 4
    import math
    d = math.sqrt(A**2 + B**2)
    print(A/d, B/d)

if __name__ == '__main__':
    main()
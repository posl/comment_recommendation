def main():
    # Get input
    ab, bc, ca = map(int, input().split())
    # Calculate area of triangle
    area = (ab * bc) // 2
    # Print area of triangle
    print(area)

if __name__ == '__main__':
    main()
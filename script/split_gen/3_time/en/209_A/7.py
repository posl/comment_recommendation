def main():
    # read in the input
    a, b = map(int, input().split())
    # print the number of integers not less than A and not more than B
    print(b - a + 1)

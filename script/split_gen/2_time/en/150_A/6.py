def main():
    # read input
    K, X = map(int, input().split())
    # check condition
    if 500 * K >= X:
        print("Yes")
    else:
        print("No")

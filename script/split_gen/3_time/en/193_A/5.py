def main():
    A, B = [int(x) for x in input().split()]
    print(100 * (1 - B / A))

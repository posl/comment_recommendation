def main():
    A, B = [int(x) for x in input().split()]
    print(A + B - (A & B))

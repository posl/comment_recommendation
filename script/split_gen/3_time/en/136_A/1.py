def main():
    A, B, C = [int(x) for x in input().split()]
    if A - B >= C:
        print(0)
    else:
        print(C - (A - B))

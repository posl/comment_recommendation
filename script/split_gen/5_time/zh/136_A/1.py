def main():
    # read inputs
    A, B, C = map(int, input().split())
    # process
    if B >= A:
        print(C)
    else:
        print(C - (A - B))

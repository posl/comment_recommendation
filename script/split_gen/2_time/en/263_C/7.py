def main():
    n, m = map(int, input().split())
    for i in range(1, m + 1):
        print(i, end="")
        if i < m:
            print(" ", end="")
        else:
            print()

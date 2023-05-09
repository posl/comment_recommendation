def main():
    # Read input
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    # Print answer
    print(p.index(x) + 1)
main()

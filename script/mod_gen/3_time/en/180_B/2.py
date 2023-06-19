def main():
    N = int(input())
    X = [int(x) for x in input().split()]
    print(sum(abs(x) for x in X))
    print((sum(x**2 for x in X))**0.5)
    print(max(abs(x) for x in X))
main()

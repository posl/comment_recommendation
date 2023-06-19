def main():
    X, N = [int(s) for s in input().split()]
    p = [int(s) for s in input().split()]
    if N == 0:
        print(X)
        return
    for i in range(101):
        if X - i not in p:
            print(X - i)
            return
        elif X + i not in p:
            print(X + i)
            return
main()

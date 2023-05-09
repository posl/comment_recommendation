def main():
    import sys
    N = int(input())
    x = list(map(int, input().split()))
    if (N != len(x)):
        print("N != len(x)")
        sys.exit()
    if (N < 1 or N > 10**5):
        print("N < 1 or N > 10**5")
        sys.exit()
    for i in range(N):
        if (x[i] < -10**5 or x[i] > 10**5):
            print("x[", i, "] < -10**5 or x[", i, "] > 10**5", sep="")
            sys.exit()
    print(sum(abs(x[i]) for i in range(N)))
    print(sum(x[i]**2 for i in range(N))**(1/2))
    print(max(abs(x[i]) for i in range(N)))

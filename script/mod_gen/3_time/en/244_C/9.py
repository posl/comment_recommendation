def main():
    N = int(input())
    a = [0] * (2*N+1)
    for i in range(1, 2*N+1):
        print(i)
        a[i] = 1
        c = int(input())
        if c == 0:
            return 0
        a[c] = 1
main()

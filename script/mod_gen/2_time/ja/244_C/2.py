def main():
    N = int(input())
    a = [0] * (2*N+1)
    for i in range(1, 2*N+1):
        if a[i] == 0:
            print(i)
            a[i] = 1
            n = int(input())
            if n == 0:
                break
            a[n] = 1
main()

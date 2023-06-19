def main():
    N = int(input())
    a = [0 for i in range(2*N+1)]
    for i in range(1,2*N+1):
        print(i)
        a[i] = 1
        x = int(input())
        if x == 0:
            break
        a[x] = 1
main()

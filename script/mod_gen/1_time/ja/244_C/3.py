def main():
    N = int(input())
    a = [0]*(2*N+2)
    for i in range(1,2*N+2):
        if a[i] == 0:
            a[i] = 1
            print(i)
            break
    for i in range(1,2*N+2):
        b = int(input())
        if b == 0:
            break
        a[b] = 1
        for j in range(1,2*N+2):
            if a[j] == 0:
                a[j] = 1
                print(j)
                break
main()

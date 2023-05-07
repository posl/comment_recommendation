def main():
    N = int(input())
    a = [0] * (2*N+1)
    for i in range(1, 2*N+1):
        print(i)
        a[i-1] = int(input())
        if a[i-1] == 0:
            return
        a[a[i-1]-1] = 1
    return

if __name__ == '__main__':
    main()
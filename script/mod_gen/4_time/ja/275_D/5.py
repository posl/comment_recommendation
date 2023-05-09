def main():
    n = int(input())
    f = [0] * (n+1)
    f[0] = 1
    for i in range(1, n+1):
        f[i] = f[i//2] + f[i//3]
    print(f[n])

if __name__ == '__main__':
    main()
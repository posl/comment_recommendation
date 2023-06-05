def main():
    N = int(input())
    for i in range(N, 10**18+1):
        if i**3 > N:
            break
        for j in range(1, 10**18+1):
            if i**3 + i**2*j + i*j**2 + j**3 > N:
                break
            if i**3 + i**2*j + i*j**2 + j**3 == N:
                print(i**3 + i**2*j + i*j**2 + j**3)
                exit()

if __name__ == '__main__':
    main()
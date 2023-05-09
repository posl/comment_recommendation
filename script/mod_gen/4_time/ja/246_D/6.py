def main():
    n = int(input())
    ans = n
    for i in range(1, 1000000):
        if i**3 > n:
            break
        for j in range(1, 1000000):
            if i**3 + i**2*j + i*j**2 + j**3 > n:
                break
            ans = max(ans, i**3 + i**2*j + i*j**2 + j**3)
    print(ans)

if __name__ == '__main__':
    main()
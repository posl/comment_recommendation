def main():
    p = int(input())
    k = 0
    for i in range(10,0,-1):
        k += p//math.factorial(i)
        p %= math.factorial(i)
    print(k)

if __name__ == '__main__':
    main()
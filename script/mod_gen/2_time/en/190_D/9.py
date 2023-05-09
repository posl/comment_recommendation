def main():
    n = int(input())
    #print(n)
    #print(n*(n-1)//2)
    #print(n*(n+1)//2)
    for i in range(1, n):
        if i*(i+1)//2 > n:
            break
    i -= 1
    print(i)

if __name__ == '__main__':
    main()
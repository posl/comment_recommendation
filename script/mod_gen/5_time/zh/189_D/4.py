def main():
    n=int(input())
    s=[input() for _ in range(n)]
    for i in range(n):
        if s[i]=="AND":
            print(2**n-2**(i+1)+1)
        else:
            print(2**(i+1))

if __name__ == '__main__':
    main()
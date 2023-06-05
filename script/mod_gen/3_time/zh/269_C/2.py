def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    else:
        n = bin(n)
        n = n[2:]
        n = list(n)
        n.reverse()
        n = ''.join(n)
        n = int(n,2)
        for i in range(0,n+1):
            i = bin(i)
            i = i[2:]
            i = list(i)
            i.reverse()
            i = ''.join(i)
            i = int(i,2)
            if i <= n:
                print(i)
            else:
                break

if __name__ == '__main__':
    main()
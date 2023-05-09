def main():
    N = int(input())
    a = set(range(1,2*N+2))
    for i in range(1,2*N+2):
        print(i)
        a.remove(i)
        b = int(input())
        if b == 0:
            return
        a.remove(b)
    return
main()

if __name__ == '__main__':
    main()
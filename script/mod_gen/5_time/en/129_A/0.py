def main():
    pqr = input().split()
    p = int(pqr[0])
    q = int(pqr[1])
    r = int(pqr[2])
    print(min(p+q, q+r, r+p))

if __name__ == '__main__':
    main()
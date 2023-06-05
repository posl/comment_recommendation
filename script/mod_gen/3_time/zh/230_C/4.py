def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q+1):
        for j in range(r, s+1):
            if (i+a-j) % 2 == 0 and (j+b-i) % 2 == 0:
                print("#", end="")
            else:
                print(".", end="")
        print()

if __name__ == '__main__':
    main()
def main():
    A,B = map(int, input().split())
    t = 0
    while A > 0:
        t += 1
        A -= B
        if A <= 0:
            break
        A = int(A ** 0.5)
    print(t)

if __name__ == '__main__':
    main()
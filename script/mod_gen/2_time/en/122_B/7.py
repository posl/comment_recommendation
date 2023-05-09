def main():
    S = input()
    l = 0
    m = 0
    for c in S:
        if c in "ACGT":
            l += 1
        else:
            l = 0
        m = max(m, l)
    print(m)

if __name__ == '__main__':
    main()
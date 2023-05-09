def main():
    S = input()
    v = 0
    w = 0
    for s in S:
        if s == 'v':
            v += 1
        else:
            w += v
    print(w)

if __name__ == '__main__':
    main()
def main():
    a, b = map(int, input().split())
    aa = str(a) * b
    bb = str(b) * a
    if aa < bb:
        print(aa)
    else:
        print(bb)

if __name__ == '__main__':
    main()
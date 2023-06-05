def main():
    line = input()
    l1, r1, l2, r2 = map(int, line.split())
    if l1 <= l2 and l2 <= r1:
        if r1 <= r2:
            print(r1 - l2)
        else:
            print(r2 - l2)
    elif l2 <= l1 and l1 <= r2:
        if r2 <= r1:
            print(r2 - l1)
        else:
            print(r1 - l1)
    else:
        print(0)

if __name__ == '__main__':
    main()
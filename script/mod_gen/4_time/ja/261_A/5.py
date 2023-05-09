def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 <= r1 and l1 <= r2:
        if l1 <= l2 and r1 <= r2:
            print(r1-l2)
        elif l2 <= l1 and r2 <= r1:
            print(r2-l1)
        elif l1 <= l2 and r2 <= r1:
            print(r2-l2)
        elif l2 <= l1 and r1 <= r2:
            print(r1-l1)
    else:
        print(0)

if __name__ == '__main__':
    main()
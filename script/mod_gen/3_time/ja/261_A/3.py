def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 <= r1 and l1 <= r2:
        print(max(l2, l1) - min(r1, r2))
    else:
        print(0)

if __name__ == '__main__':
    main()
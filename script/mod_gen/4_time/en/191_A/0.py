def main():
    v, t, s, d = map(int, input().split())
    if d / v >= t and d / v <= s:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()
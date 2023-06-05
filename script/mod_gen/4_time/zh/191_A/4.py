def main():
    v, t, s, d = map(int, input().split())
    # print(v, t, s, d)
    # print((d/v))
    if (d/v) >= t and (d/v) <= s:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()
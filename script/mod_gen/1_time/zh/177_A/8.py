def main():
    d, t, s = (int(i) for i in input().split())
    if d <= t * s:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
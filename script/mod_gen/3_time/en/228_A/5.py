def main():
    s, t, x = map(int, input().split())
    if s <= x <= t:
        print("Yes")
    elif t < s and (x >= s or x <= t):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
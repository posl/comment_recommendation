def main():
    s, t, x = map(int, input().split())
    if x < s:
        print("No")
    elif x >= t:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()
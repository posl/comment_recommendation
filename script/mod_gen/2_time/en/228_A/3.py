def main():
    s, t, x = map(int, input().split())
    if (s < t):
        if (s < x and x < t):
            print("Yes")
        else:
            print("No")
    elif (t < s):
        if (s < x or x < t):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()
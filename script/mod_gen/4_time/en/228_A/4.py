def main():
    s, t, x = map(int, input().split())
    if s < t:
        print("Yes") if s < x < t else print("No")
    else:
        print("Yes") if s < x or x < t else print("No")

if __name__ == '__main__':
    main()
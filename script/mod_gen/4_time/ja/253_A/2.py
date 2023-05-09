def main():
    a, b, c = map(int, input().split())
    if b == max(a, b, c) or b == min(a, b, c):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()
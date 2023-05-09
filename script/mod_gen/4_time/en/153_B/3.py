def main():
    h, n = map(int, input().split())
    a = map(int, input().split())
    if h <= sum(a):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
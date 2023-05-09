def main():
    h, n = map(int, input().split())
    arr = list(map(int, input().split()))
    if h <= sum(arr):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
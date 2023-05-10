def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    if li[-1] < sum(li[:-1]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
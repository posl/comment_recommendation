def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[-1] < sum(l[:-1]):
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()
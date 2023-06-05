def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    a.sort(reverse=True)
    if a[m-1] >= sum_a/(4*m):
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()
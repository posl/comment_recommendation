def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum_a = sum(a)
    for i in range(m):
        if a[i] < sum_a / (4 * m):
            print("否")
            break
    else:
        print("是")

if __name__ == '__main__':
    main()
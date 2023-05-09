def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(k):
        a[b[i] - 1] = 0
    if sum(a) > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
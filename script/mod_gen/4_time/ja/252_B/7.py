def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    like = [0] * n
    for i in range(k):
        like[b[i] - 1] = 1
    max = 0
    for i in range(n):
        if like[i] == 0 and max < a[i]:
            max = a[i]
    if max == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()
def main():
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[1]+a[2]+a[3])
main()

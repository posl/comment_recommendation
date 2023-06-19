def main():
    # Get input here
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    # Calculate result here
    # print(n, k)
    # print(a)
    for i in range(n - k):
        if a[i] > a[i + k]:
            print('Yes')
            break
    else:
        print('No')
    # Print output here
main()

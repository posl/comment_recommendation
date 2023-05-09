def main():
    # input
    a = list(map(int, input().split()))
    # compute
    ans = a[0]
    for i in range(3):
        ans = a[ans]
    # output
    print(ans)

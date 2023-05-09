def main():
    # input
    a = list(map(int, input().split()))
    # compute
    k = 0
    for i in range(3):
        k = a[k]
    # output
    print(k)

def main():
    # input
    a = list(map(int, input().split()))
    # compute
    for i in range(3):
        a = a[a[0]]
        # output
    print(a)

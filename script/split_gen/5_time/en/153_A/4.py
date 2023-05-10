def main():
    # input
    H, A = map(int, input().split())
    # compute
    count = H // A
    if H % A != 0:
        count += 1
    # output
    print(count)

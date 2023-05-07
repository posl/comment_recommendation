def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    # compute
    inv_sum = 0
    for A in As:
        inv_sum += 1/A
    # output
    print(1/inv_sum)

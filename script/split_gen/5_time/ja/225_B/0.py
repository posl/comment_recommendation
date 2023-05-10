def main():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N-1)]
    ab = sorted(ab)
    # print(ab)
    # print(ab[0][1])
    # print(ab[-1][1])
    if ab[0][1] == ab[-1][1]:
        print('Yes')
    else:
        print('No')

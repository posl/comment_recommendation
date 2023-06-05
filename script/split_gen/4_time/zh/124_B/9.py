def main():
    # input
    N = int(input())
    H = [int(n) for n in input().split()]
    # print(N)
    # print(H)
    # count
    count = 0
    max = 0
    for i in range(N):
        if max <= H[i]:
            count += 1
        if max < H[i]:
            max = H[i]
    print(count)

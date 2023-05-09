def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        if H[i] >= max(H[i:]):
            count += 1
    print(count)

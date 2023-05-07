def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
            continue
        for j in range(i):
            if H[i] < H[j]:
                break
        else:
            count += 1
    print(count)

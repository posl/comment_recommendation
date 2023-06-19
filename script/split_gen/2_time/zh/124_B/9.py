def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    count = 1
    for i in range(1,N):
        if max(H[:i]) <= H[i]:
            count += 1
    print(count)

def main():
    N = int(input())
    H = list(map(int, input().split()))
    H.reverse()
    for i in range(1, N):
        if H[i - 1] - H[i] > 1:
            print('No')
            return
        elif H[i - 1] - H[i] == 1:
            H[i] += 1
    print('Yes')
    return

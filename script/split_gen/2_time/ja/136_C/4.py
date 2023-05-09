def main():
    N = int(input())
    H = list(map(int, input().split()))
    H.append(0)
    for i in range(N):
        if H[i] < H[i + 1]:
            H[i + 1] -= 1
        elif H[i] > H[i + 1]:
            print("No")
            return
    print("Yes")
    return

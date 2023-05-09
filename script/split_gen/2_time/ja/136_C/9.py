def main():
    N = int(input())
    H = list(map(int, input().split()))
    # ここに処理を書く
    for i in range(N-1):
        if H[i] > H[i+1]:
            print("No")
            exit()
        elif H[i] == H[i+1]:
            pass
        else:
            H[i+1] -= 1
    print("Yes")

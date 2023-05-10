def main():
    N = int(input())
    H = list(map(int, input().split()))
    current_height = H[0]
    for i in range(1, N):
        if current_height < H[i]:
            current_height = H[i]
    print(current_height)

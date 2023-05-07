def main():
    N = int(input())
    # 1円引き出しの回数
    count = N
    # 6円引き出しの回数
    for i in range(1, 6):
        if N >= 6 ** i:
            count = min(count, 1 + main(N - 6 ** i))
        else:
            break
    # 9円引き出しの回数
    for i in range(1, 6):
        if N >= 9 ** i:
            count = min(count, 1 + main(N - 9 ** i))
        else:
            break
    return count

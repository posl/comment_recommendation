def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    # 橋を取り除く必要のある島の最大値
    max_remove = 0
    # 橋を取り除く必要のある島の最小値
    min_remove = N
    # 橋を取り除く必要のある島の個数
    remove_count = 0
    for i in range(1, N):
        for j in range(M):
            if AB[j][0] == i or AB[j][1] == i:
                remove_count += 1
        if remove_count < min_remove:
            min_remove = remove_count
        if remove_count > max_remove:
            max_remove = remove_count
        remove_count = 0
    print(min_remove)

if __name__ == '__main__':
    main()
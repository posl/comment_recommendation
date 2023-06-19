def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    # 1の場所を配列に格納
    one_pos = []
    for i in range(60):
        if (n >> i) & 1:
            one_pos.append(i)
    # 1の場所の組み合わせをbit全探索
    for i in range(1 << len(one_pos)):
        x = 0
        for j in range(len(one_pos)):
            if (i >> j) & 1:
                x += 1 << one_pos[j]
        print(x)
main()

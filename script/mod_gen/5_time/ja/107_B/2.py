def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    # 行の削除
    a = [row for row in a if "#" in row]
    # 列の削除
    a = list(map(list, zip(*a)))
    a = [col for col in a if "#" in col]
    a = list(map(list, zip(*a)))
    for row in a:
        print("".join(row))

if __name__ == '__main__':
    main()
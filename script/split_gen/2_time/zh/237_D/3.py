def main():
    n = int(input())
    s = input()
    # 0のリストを作成
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i + 1)
        else:
            a.append(i + 1)
    # 結果を出力
    print(*a)

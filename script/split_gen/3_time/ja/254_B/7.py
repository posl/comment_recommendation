def main():
    N = int(input())
    # 1行目
    print(1)
    # 2行目以降
    for i in range(1, N):
        # 1つ目の要素
        print(1, end=" ")
        # 2つ目以降の要素
        for j in range(1, i+1):
            if j == i:
                print(1)
            else:
                print(j+1, end=" ")

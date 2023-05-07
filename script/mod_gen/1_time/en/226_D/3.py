def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    #print(x)
    #print(y)
    
    # (a, b) について、(x_i + a, y_i + b) が全て異なるような a, b の組み合わせを求める
    # これは、(x_i + a, y_i + b) が全て異なるような a, b の組み合わせが 2N 個以上あればいい
    # これは、(x_i, y_i) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # これは、(x_i, y_i) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # (x_i, y_i) が全て異なるような a, b の組み合わせは、(x_i - x_j, y_i - y_j) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # (x_i, y_i) が全て異なるような a, b の組み合わせは、(x_i - x_j, y_i - y_j) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # (x_i, y_i) が全て異なるような a, b の組み合わせは、(x_i - x_j, y_i - y_j) が全て異なるような a, b の組み合わせが N 個以上あればいい
    # (x_i, y_i) が全

if __name__ == '__main__':
    main()
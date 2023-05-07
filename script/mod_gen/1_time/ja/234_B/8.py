def main():
    import sys
    import math
    #入力
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    #処理
    max = 0.0
    for i in range(N):
        for j in range(i+1, N):
            dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            if dist > max:
                max = dist
    #出力
    print(max)

if __name__ == '__main__':
    main()
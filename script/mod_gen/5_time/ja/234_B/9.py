def main():
    import sys
    import math
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max_len = 0
    for i in range(N-1):
        for j in range(i+1, N):
            len_i_j = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if len_i_j > max_len:
                max_len = len_i_j
    print(max_len)

if __name__ == '__main__':
    main()
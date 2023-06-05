def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = [0] * n
    for i in range(1, n, 2):
        b_list[0] += a_list[i]
    for i in range(1, n):
        b_list[i] = a_list[i - 1] * 2 - b_list[i - 1]
    print(' '.join(map(str, b_list)))

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split(' '))))
    left = 0
    right = 0
    for i in range(n):
        left = left + ab[i][0] / ab[i][1]
    for i in range(n - 1, -1, -1):
        right = right + ab[i][0] / ab[i][1]
    print(left / 2 + right / 2)

def main():
    N = int(input())
    LR = []
    for _ in range(N):
        LR.append(list(map(int, input().split())))
    LR.sort(key=lambda x: x[0])
    left = LR[0][0]
    right = LR[0][1]
    for i in range(1, N):
        if LR[i][0] <= right:
            right = max(right, LR[i][1])
        else:
            print(left, right)
            left = LR[i][0]
            right = LR[i][1]
    print(left, right)

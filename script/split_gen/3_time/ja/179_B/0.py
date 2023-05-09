def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            count += 1
    if count >= 1:
        print("Yes")
    else:
        print("No")

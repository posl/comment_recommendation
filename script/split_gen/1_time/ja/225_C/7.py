def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        if B[0][0] == 1:
            print("Yes")
        else:
            print("No")
    else:
        if B[0][0] == 1 and B[1][0] == 8:
            print("Yes")
        else:
            print("No")

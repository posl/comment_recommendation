def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    answer = 0
    if R == 1 and C == 1:
        answer = 0
    elif R == 1 and C == W:
        answer = 0
    elif R == H and C == 1:
        answer = 0
    elif R == H and C == W:
        answer = 0
    elif R == 1:
        answer = 1
    elif R == H:
        answer = 1
    elif C == 1:
        answer = 1
    elif C == W:
        answer = 1
    else:
        answer = 2
    print(answer)

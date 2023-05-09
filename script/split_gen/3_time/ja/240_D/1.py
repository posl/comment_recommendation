def main():
    N = int(input())
    A = list(map(int, input().split()))
    balls = []
    for i in range(N):
        if len(balls) == 0:
            balls.append([A[i], 1])
        else:
            if balls[-1][0] == A[i]:
                balls[-1][1] += 1
                if balls[-1][1] == balls[-1][0]:
                    balls.pop()
            else:
                balls.append([A[i], 1])
        print(len(balls))

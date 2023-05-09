def main():
    N = int(input())
    scores = []
    for i in range(N):
        S, T = input().split()
        T = int(T)
        scores.append([i, S, T])
    scores.sort(key=lambda x: x[1])
    scores.sort(key=lambda x: x[2], reverse=True)
    for i in range(N):
        if scores[i][0] == 0:
            print(i + 1)
            break

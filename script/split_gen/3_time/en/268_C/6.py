def main():
    N = int(input())
    P = list(map(int, input().split()))
    happy = 0
    for i in range(1, N-1):
        if P[i-1] < P[i] < P[i+1] or P[i-1] > P[i] > P[i+1]:
            happy += 1
    if P[N-2] < P[N-1] < P[0] or P[N-2] > P[N-1] > P[0]:
        happy += 1
    if P[N-1] < P[0] < P[1] or P[N-1] > P[0] > P[1]:
        happy += 1
    print(happy)

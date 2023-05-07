def main():
    N = int(input())
    A = list(map(int, input().split()))
    angle = 360
    for i in range(N):
        angle = min(angle, 2*abs(angle-A[i]))
    print(angle)

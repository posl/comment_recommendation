def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = 0
    B = 0
    for i in range(N):
        A += AB[i][0]/AB[i][1]
        B += 1/AB[i][1]
    print(A/B)

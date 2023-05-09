def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    #print(AB)
    A, B = 0, 0
    for i in range(N):
        if i % 2 == 0:
            A += AB[i][0]
        else:
            B += AB[i][1]
    print(A - B)

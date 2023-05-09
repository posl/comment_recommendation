def main():
    N = int(input())
    AB = [[int(i) for i in input().split()] for j in range(N)]
    time = 0
    for i in range(N):
        time += AB[i][0] / AB[i][1]
    time /= 2
    dist = 0
    for i in range(N):
        if time >= AB[i][0] / AB[i][1]:
            dist += AB[i][0]
        else:
            dist += AB[i][1] * time
    print(dist)

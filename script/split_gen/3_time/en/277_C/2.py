def main():
    n = int(input())
    ladders = []
    for i in range(n):
        a, b = map(int, input().split())
        ladders.append([a, b])
    ladders.sort()
    #print(ladders)
    a = ladders[0][0]
    b = ladders[0][1]
    for i in range(1, n):
        if ladders[i][0] <= a and a <= ladders[i][1]:
            a = ladders[i][0]
            b = ladders[i][1]
        elif ladders[i][0] <= b and b <= ladders[i][1]:
            a = ladders[i][0]
            b = ladders[i][1]
        else:
            a = ladders[i][0]
            b = ladders[i][1]
    print(b)

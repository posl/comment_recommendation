def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    count = 0
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            count += 1
    if count > 0:
        print("Yes")
    else:
        print("No")

def main():
    n = int(input())
    num = []
    for i in range(n):
        num.append(input().split())
    for i in range(n):
        num[i][0] = int(num[i][0])
        for j in range(num[i][0]):
            num[i][j+1] = int(num[i][j+1])
    num.sort(key=lambda x: x[1:])
    count = 1
    for i in range(n-1):
        if num[i] != num[i+1]:
            count += 1
    print(count)

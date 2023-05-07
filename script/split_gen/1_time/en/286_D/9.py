def main():
    n,x = map(int, input().split())
    temp = []
    for i in range(n):
        temp.append(list(map(int, input().split())))
    sum = 0
    for i in range(n):
        sum += temp[i][0]*temp[i][1]
    if sum <= x:
        print("Yes")
    else:
        print("No")

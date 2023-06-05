def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
                print("Yes")
                return
    print("No")
    return

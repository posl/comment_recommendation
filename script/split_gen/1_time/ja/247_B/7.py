def main():
    N = int(input())
    data = [input().split() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if data[i][0] == data[j][0] or data[i][1] == data[j][1]:
                    print("No")
                    return
    print("Yes")
    return

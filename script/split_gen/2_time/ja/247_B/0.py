def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(N):
            if name[i][0] == name[j][0] or name[i][1] == name[j][1]:
                if i != j:
                    print("No")
                    return
    print("Yes")

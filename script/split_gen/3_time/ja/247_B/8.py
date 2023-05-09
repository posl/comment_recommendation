def main():
    n = int(input())
    name = [input().split() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and name[i][0] == name[j][0] and name[i][1] == name[j][1]:
                print("No")
                return
    print("Yes")

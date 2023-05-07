def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(N):
            if i != j and (names[i][0] == names[j][0] or names[i][1] == names[j][1]):
                print("Yes")
                return
    print("No")

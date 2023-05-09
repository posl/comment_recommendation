def main():
    N = int(input())
    names = [input().split() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    print("No")
                    return
    print("Yes")

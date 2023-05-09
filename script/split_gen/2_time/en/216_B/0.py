def main():
    n = int(input())
    names = [input().split() for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                return
    print("No")

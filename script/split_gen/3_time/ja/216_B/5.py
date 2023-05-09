def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    name.sort()
    for i in range(n-1):
        if name[i][0] == name[i+1][0] and name[i][1] == name[i+1][1]:
            print("Yes")
            return
    print("No")
    return

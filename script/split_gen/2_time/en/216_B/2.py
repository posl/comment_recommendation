def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(i+1,N):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                return
    print("No")
    return

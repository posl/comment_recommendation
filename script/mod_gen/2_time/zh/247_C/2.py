def problem247_b():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(N):
            if name[i][0] == name[j][1] and i != j:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    problem247_b()
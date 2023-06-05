def main():
    N, M = map(int, input().split())
    x = []
    for i in range(M):
        x.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(i+1, N):
            flag = False
            for k in range(M):
                if i+1 in x[k] and j+1 in x[k]:
                    flag = True
            if not flag:
                print("No")
                return
    print("Yes")

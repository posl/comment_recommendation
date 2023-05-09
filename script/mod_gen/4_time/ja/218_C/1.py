def check(S,T):
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                return False
    return True
N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]
# print(S)
# print(T)
# print(check(S,T))
for _ in range(4):
    T = list(map(list,zip(*T[::-1])))
    if check(S,T):
        print("Yes")
        exit()
print("No")

if __name__ == '__main__':
    check()
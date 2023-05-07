def main():
    H,W = map(int,input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    S.sort()
    T.sort()
    if S == T:
        print("Yes")
    else:
        print("No")

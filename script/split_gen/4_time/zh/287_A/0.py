def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S[i] == "For":
            print("Yes")
            break
        elif S[i] == "Against":
            print("No")
            break

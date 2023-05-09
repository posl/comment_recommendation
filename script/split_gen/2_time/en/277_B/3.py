def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(S) != len(set(S)):
        print("No")
        return
    for i in range(N):
        if S[i][0] not in "HDCS" or S[i][1] not in "A23456789TJQK":
            print("No")
            return
    print("Yes")

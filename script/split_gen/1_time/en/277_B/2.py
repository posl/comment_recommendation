def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(S) != len(set(S)):
        print("No")
        return
    for s in S:
        if s[0] not in ["H", "D", "C", "S"]:
            print("No")
            return
        if s[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            print("No")
            return
    print("Yes")

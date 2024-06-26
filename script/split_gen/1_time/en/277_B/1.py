def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(set(S)) != N:
        print("No")
        return
    for s in S:
        if s[0] not in "HDCS":
            print("No")
            return
        if s[1] not in "A23456789TJQK":
            print("No")
            return
    print("Yes")

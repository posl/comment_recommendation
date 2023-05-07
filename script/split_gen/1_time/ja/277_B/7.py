def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(set(S)) != N:
        print("No")
        return
    if not all([s[0] in "HDCS" for s in S]):
        print("No")
        return
    if not all([s[1] in "A23456789TJQK" for s in S]):
        print("No")
        return
    print("Yes")

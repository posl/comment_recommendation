def main():
    n = int(input())
    s = [input() for _ in range(n)]
    if len(set(s)) != n:
        print("No")
        return
    for i in range(n):
        if s[i][0] not in "HDCS":
            print("No")
            return
        if s[i][1] not in "A23456789TJQK":
            print("No")
            return
    print("Yes")

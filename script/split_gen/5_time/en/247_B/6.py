def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input().split())
    for i in range(n):
        for j in range(n):
            if s[i][0] == s[j][0] and i != j:
                print("Yes")
                return
            if s[i][1] == s[j][1] and i != j:
                print("Yes")
                return
    print("No")
    return

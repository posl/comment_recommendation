def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] == "For":
            print("Yes")
            break
        elif s[i] == "Against":
            print("No")
            break

def main():
    n = int(input())
    names = set()
    for i in range(n):
        s, t = input().split()
        names.add(s)
        names.add(t)
    if len(names) == n:
        print("Yes")
    else:
        print("No")

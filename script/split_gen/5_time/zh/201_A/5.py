def main():
    l = input().split()
    l = list(map(int, l))
    l.sort()
    if l[2] - l[1] == l[1] - l[0]:
        print("Yes")
    else:
        print("No")

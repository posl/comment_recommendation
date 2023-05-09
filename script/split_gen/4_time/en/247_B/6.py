def main():
    n = int(input())
    nicknames = []
    for i in range(n):
        s, t = input().split()
        nicknames.append(s)
        nicknames.append(t)
    if len(nicknames) == len(set(nicknames)):
        print("Yes")
    else:
        print("No")

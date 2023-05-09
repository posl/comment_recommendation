def main():
    s = input()
    t = input()
    l = len(s)
    cnt = 0
    for i in range(l):
        if s[i] != t[i]:
            cnt += 1
    if cnt == 0 or cnt == 2:
        print("Yes")
    else:
        print("No")

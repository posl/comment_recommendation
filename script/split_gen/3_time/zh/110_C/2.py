def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if s != t:
        print("No")
        return
    print("Yes")

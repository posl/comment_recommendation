def main():
    s = input()
    if len(s) != 4:
        return
    if len(set(s)) != 2:
        return
    for c in set(s):
        if s.count(c) != 2:
            return
    print("Yes")

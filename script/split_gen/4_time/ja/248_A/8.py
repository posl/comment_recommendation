def main():
    s = input()
    s = list(s)
    s.sort()
    s = list(map(int, s))
    for i in range(1, 10):
        if i not in s:
            print(i)
            return

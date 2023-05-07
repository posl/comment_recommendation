def main():
    s = input()
    s = list(map(int, s))
    s = sorted(s)
    for i in range(10):
        if i not in s:
            print(i)
            break

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    for i in s:
        if i[0] == '!':
            if i[1:] in s:
                print(i[1:])

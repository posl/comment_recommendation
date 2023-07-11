def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if i[0] == '!':
            if i[1:] in s:
                pr

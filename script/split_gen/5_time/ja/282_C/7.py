def main():
    n = int(input())
    s = input()
    t = ""
    cnt = 0
    for c in s:
        if c == '"':
            cnt += 1
        if cnt % 2 == 1 and c == ',':
            c = '.'
        t += c
    print(t)

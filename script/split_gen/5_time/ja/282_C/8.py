def main():
    n = int(input())
    s = input()
    cnt = 0
    for c in s:
        if c == '"':
            cnt += 1
    if cnt % 2 != 0:
        print("error")
        return
    cnt //= 2
    ret = ""
    for c in s:
        if c == ',' and cnt > 0:
            c = '.'
            cnt -= 1
        ret += c
    print(ret)

def main():
    n = int(input())
    s = input()
    ans = ""
    q = 0
    for c in s:
        if c == '"':
            q += 1
        elif q % 2 == 0 and c == ',':
            ans += '.'
        else:
            ans += c
    print(ans)

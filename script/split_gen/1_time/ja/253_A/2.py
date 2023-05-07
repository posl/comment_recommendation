def main():
    a, b, c = map(int, input().split())
    if b < a:
        a, b = b, a
    if c < a:
        a, c = c, a
    if c < b:
        b, c = c, b
    if b == a or b == c:
        print('Yes')
    else:
        print('No')

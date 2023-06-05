def compare(a, b):
    if a > b:
        return ">"
    elif a < b:
        return "<"
    else:
        return "="
a, b, c = map(int, input().split())
print(compare(pow(a, c), pow(b, c)))

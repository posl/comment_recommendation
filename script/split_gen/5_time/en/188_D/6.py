def main():
    n, c = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(n)]
    abc.sort(key=lambda x: x[0])
    abc.sort(key=lambda x: x[2])
    total = 0
    day = 0
    fee = 0
    for a, b, c in abc:
        if day == a and fee == c:
            continue
        total += (a - day) * min(c, fee)
        day = a
        fee = c
        total += c * (b - a + 1)
        day = b + 1
    print(total)

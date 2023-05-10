def main():
    k = int(input())
    h = 21
    m = 0
    m = m + (k % 60)
    h = h + (k // 60)
    if m >= 60:
        h = h + 1
        m = m - 60
    if h >= 24:
        h = h - 24
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    print(str(h) + ":" + str(m))

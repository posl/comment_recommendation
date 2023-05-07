def main():
    k = int(input())
    h = 21
    m = k
    if m >= 60:
        h = h + m // 60
        m = m % 60
    if h >= 24:
        h = h % 24
    print('{0:02d}:{1:02d}'.format(h, m))

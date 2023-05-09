def main():
    k = int(input())
    h = k // 60
    m = k % 60
    if h >= 24:
        h = h % 24
    print('{:02d}:{:02d}'.format(h, m))

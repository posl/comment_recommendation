def main():
    k = int(input())
    h = 21 + (k // 60)
    m = k % 60
    print('{0:02d}:{1:02d}'.format(h, m))

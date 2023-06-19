def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{0:02d}:{1:02d}".format(21+h%24,m))
    return

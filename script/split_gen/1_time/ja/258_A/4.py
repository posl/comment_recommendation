def main():
    k = int(input())
    print("{0:02d}:{1:02d}".format((21 + (k // 60)) % 24, (k % 60)))

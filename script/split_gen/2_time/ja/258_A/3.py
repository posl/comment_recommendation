def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02}:{:02}".format(h + 21, m))

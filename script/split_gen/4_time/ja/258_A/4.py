def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:0>2}:{:0>2}".format(h + 21, m))

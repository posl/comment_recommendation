def main():
    a, b = map(int, input().split())
    print("{:03}".format(round(b/a, 3)*1000))

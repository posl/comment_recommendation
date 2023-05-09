def main():
    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    print((a*b*c)/((a*b)+(b*c)+(c*a)))

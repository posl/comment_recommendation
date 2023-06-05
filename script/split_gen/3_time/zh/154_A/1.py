def main():
    s = input()
    a,b = map(int, input().split())
    t = input()
    u = input()
    if t == u:
        print(a-1, b)
    else:
        print(a, b-1)

def main():
    n = input()
    a = map(int, raw_input().split())
    a = list(set(a))
    print len(a)

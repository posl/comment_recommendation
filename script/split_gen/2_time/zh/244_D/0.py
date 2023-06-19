def main():
    s = input().strip().split()
    t = input().strip().split()
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')

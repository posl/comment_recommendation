def main():
    a = map(int, raw_input().split())
    if sum(a) >= 22:
        print 'bust'
    else:
        print 'win'

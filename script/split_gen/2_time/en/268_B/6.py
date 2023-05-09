def main():
    s = input()
    t = input()
    if s in t[:len(s)]:
        print('Yes')
    else:
        print('No')

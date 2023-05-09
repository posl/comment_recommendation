def main():
    s = input().split()
    t = input().split()
    if len(set(s)) == len(set(t)) == 3:
        print('Yes')
    elif len(set(s)) == 2 and len(set(t)) == 2:
        print('Yes')
    else:
        print('No')

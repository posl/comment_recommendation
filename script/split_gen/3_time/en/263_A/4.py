def main():
    a = input().split()
    a = [int(i) for i in a]
    if len(set(a)) == 2:
        if max(a.count(i) for i in set(a)) == 3:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

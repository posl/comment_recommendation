def main():
    s = input()
    if len(s) == 4:
        if len(set(s)) == 2:
            for i in set(s):
                if s.count(i) != 2:
                    print('No')
                    break
            else:
                print('Yes')
        else:
            print('No')
    else:
        print('No')

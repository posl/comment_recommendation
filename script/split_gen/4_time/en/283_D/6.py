def main():
    s = input()
    s = s.replace('()','')
    while s != '':
        if s.count('()') == 0:
            print('No')
            return
        s = s.replace('()','')
    print('Yes')
    return

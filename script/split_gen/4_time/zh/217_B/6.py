def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set()
    s.add(s1)
    s.add(s2)
    s.add(s3)
    if 'ABC' not in s:
        print('ABC')
    elif 'ARC' not in s:
        print('ARC')
    elif 'AGC' not in s:
        print('AGC')
    else:
        print('AHC')

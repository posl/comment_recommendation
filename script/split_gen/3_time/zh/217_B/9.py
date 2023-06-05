def solution():
    s = []
    for i in range(3):
        s.append(input())
    if 'ABC' not in s:
        print('ABC')
    elif 'ARC' not in s:
        print('ARC')
    elif 'AGC' not in s:
        print('AGC')
    elif 'AHC' not in s:
        print('AHC')

def solve():
    s = input()
    n = len(s)
    s = s.replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '').replace('i', '').replace('j', '').replace('k', '').replace('l', '').replace('m', '').replace('n', '').replace('o', '').replace('p', '').replace('q', '').replace('r', '').replace('s', '').replace('t', '').replace('u', '').replace('v', '').replace('w', '').replace('x', '').replace('y', '').replace('z', '')
    n = len(s)
    if n == 0:
        print('是')
    else:
        print('否')

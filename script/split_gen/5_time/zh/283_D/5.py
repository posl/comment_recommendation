def main():
    s = input()
    s = s.replace('a','')
    s = s.replace('b','')
    s = s.replace('c','')
    s = s.replace('d','')
    s = s.replace('e','')
    s = s.replace('f','')
    s = s.replace('g','')
    s = s.replace('h','')
    s = s.replace('i','')
    s = s.replace('j','')
    s = s.replace('k','')
    s = s.replace('l','')
    s = s.replace('m','')
    s = s.replace('n','')
    s = s.replace('o','')
    s = s.replace('p','')
    s = s.replace('q','')
    s = s.replace('r','')
    s = s.replace('s','')
    s = s.replace('t','')
    s = s.replace('u','')
    s = s.replace('v','')
    s = s.replace('w','')
    s = s.replace('x','')
    s = s.replace('y','')
    s = s.replace('z','')
    while True:
        if s.find('()') == -1:
            break
        else:
            s = s.replace('()','')
    if s == '':
        print('是')
    else:
        print('否')

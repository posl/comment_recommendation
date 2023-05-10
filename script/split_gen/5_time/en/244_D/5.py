def main():
    #s = input()
    #s = s.split()
    #t = input()
    #t = t.split()
    s = ['R', 'G', 'B']
    t = ['R', 'G', 'B']
    for i in range(3):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

def problems267_b():
    s = input()
    print('Yes' if s[0]=='0' and s.count('1')>0 and s.count('0')>0 else 'No')

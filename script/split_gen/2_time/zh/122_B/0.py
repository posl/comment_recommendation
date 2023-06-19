def problem122_b(s):
    #print(s)
    s = s.replace('A','1')
    s = s.replace('C','2')
    s = s.replace('G','3')
    s = s.replace('T','4')
    #print(s)
    s = s.replace('1','A')
    s = s.replace('2','C')
    s = s.replace('3','G')
    s = s.replace('4','T')
    #print(s)
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            #print(s[i:j])
            if s[i:j].find('B') == -1 and s[i:j].find('D') == -1 and s[i:j].find('E') == -1 and s[i:j].find('F') == -1 and s[i:j].find('H') == -1 and s[i:j].find('I') == -1 and s[i:j].find('J') == -1 and s[i:j].find('K') == -1 and s[i:j].find('L') == -1 and s[i:j].find('M') == -1 and s[i:j].find('N') == -1 and s[i:j].find('O') == -1 and s[i:j].find('P') == -1 and s[i:j].find('Q') == -1 and s[i:j].find('R') == -1 and s[i:j].find('S') == -1 and s[i:j].find('U') == -1 and s[i:j].find('V') == -1 and s[i:j].find('W') == -1 and s[i:j].find('X') == -1 and s[i:j].find('Y') == -1 and s[i:j].find('Z') == -1:
                max_len = max(max_len,len(s[i:j]))
    print(max_len)

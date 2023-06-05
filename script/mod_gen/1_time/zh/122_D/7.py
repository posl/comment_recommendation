def check(s):
    for i in range(len(s)-2):
        if s[i]=='A' and s[i+1]=='G' and s[i+2]=='C': return False
        if s[i]=='A' and s[i+1]=='C' and s[i+2]=='G': return False
        if s[i]=='G' and s[i+1]=='A' and s[i+2]=='C': return False
        if s[i]=='A' and s[i+1]=='G' and s[i+2]=='C': return False
        if s[i]=='A' and s[i+1]=='C' and s[i+2]=='G': return False
        if s[i]=='C' and s[i+1]=='A' and s[i+2]=='G': return False
    return True

if __name__ == '__main__':
    check()
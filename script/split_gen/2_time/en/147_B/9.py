def hugs(s):
    return sum(1 for i in xrange(len(s)/2) if s[i] != s[-i-1])

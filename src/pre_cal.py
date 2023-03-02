import Levenshtein
import os
import re

with open('../pre_research/problem_281/a/sample.py', 'r') as f:
    a = f.readlines()
    b = [s for s in a if not s.startswith('#')]
    c = list(map(lambda x: re.split('\n|\s', x), b))
    d =[]
    for s in c:
        s = list(filter(lambda x: x != '', s))
        d.extend(s)
    
    text1 = ''.join(d)

with open('../pre_research/problem_281/a/sample2.py', 'r') as f:
    a = f.readlines()
    b = [s for s in a if not s.startswith('#')]
    c = list(map(lambda x: re.split('\n|\s', x), b))
    d =[]
    for s in c:
        s = list(filter(lambda x: x != '', s))
        d.extend(s)
    
    text2 = ''.join(d)
    
print(Levenshtein.ratio(text1, text2))
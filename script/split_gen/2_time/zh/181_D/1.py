def judge(s):
    for i in range(1,10):
        if s.count(str(i))>0:
            if i%8==0:
                return True
    return False
s=input()

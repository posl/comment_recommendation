def check(s1,s2,s3):
    num = set(s1 + s2 + s3)
    if len(num) > 10:
        return False
    num = list(num)
    for i in range(10):
        s1 = s1.replace(num[i],str(i))
        s2 = s2.replace(num[i],str(i))
        s3 = s3.replace(num[i],str(i))
    if int(s1) + int(s2) == int(s3):
        return True
    else:
        return False
s1 = input()
s2 = input()
s3 = input()

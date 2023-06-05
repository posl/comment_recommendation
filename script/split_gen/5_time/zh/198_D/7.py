def solve(s1,s2,s3):
    if len(s1)>len(s3) or len(s2)>len(s3):
        return "UNSOLVABLE"
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    s1 = s1 + '0'*(len(s3)-len(s1))
    s2 = s2 + '0'*(len(s3)-len(s2))
    s3 = s3 + '0'*(len(s3)-len(s3))
    s1 = s1.replace(s1[0],str(0))
    s2 = s2.replace(s2[0],str(0))
    s3 = s3.replace(s3[0],str(0))
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if int(s1.replace(s1[0],str(i))) + int(s2.replace(s2[0],str(j))) == int(s3.replace(s3[0],str(k))):
                    return int(s1.replace(s1[0],str(i))),int(s2.replace(s2[0],str(j))),int(s3.replace(s3[0],str(k)))
    return "UNSOLVABLE"
s1 = input()
s2 = input()
s3 = input()
print(*solve(s1,s2,s3),sep='\n')

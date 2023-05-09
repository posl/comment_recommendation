def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    s1 = s1.replace('x', '0')
    s2 = s2.replace('x', '0')
    s3 = s3.replace('x', '0')
    s1 = s1.replace('y', '0')
    s2 = s2.replace('y', '0')
    s3 = s3.replace('y', '0')
    s1 = s1.replace('z', '0')
    s2 = s2.replace('z', '0')
    s3 = s3.replace('z', '0')
    if int(s1) + int(s2) == int(s3):
        print(s1[::-1])
        print(s2[::-1])
        print(s3[::-1])
    else:
        print('UNSOLVABLE')

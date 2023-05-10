def main():
    n = int(input())
    s = input()
    s1 = s.replace(',','.')
    s2 = s1.split('"')
    for i in range(len(s2)):
        if i%2 == 1:
            s2[i] = s2[i].replace('.','"')
    s3 = '"'.join(s2)
    print(s3)

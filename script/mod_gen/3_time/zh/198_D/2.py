def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1+s2+s3)
    if len(s) > 10:
        print('UNSOLVABLE')
        exit()
    s = list(s)
    if len(s) < 10:
        for i in range(10-len(s)):
            s.append('0')
    for i in range(10):
        s[i] = ord(s[i])-ord('a')
    for i in range(1000,10000):
        if len(set(str(i))) != 4:
            continue
        n1 = i
        n2 = i*2
        n3 = i*3
        if len(str(n2)) != len(str(n1)):
            continue
        if len(str(n3)) != len(str(n1)):
            continue
        for j in range(4):
            if s1[j] == chr(n1//(10**(3-j))%10 + ord('a')):
                continue
            else:
                break
        else:
            for j in range(4):
                if s2[j] == chr(n2//(10**(3-j))%10 + ord('a')):
                    continue
                else:
                    break
            else:
                for j in range(4):
                    if s3[j] == chr(n3//(10**(3-j))%10 + ord('a')):
                        continue
                    else:
                        break
                else:
                    print(n1)
                    print(n2)
                    print(n3)
                    exit()
    print('UNSOLVABLE')
    exit()

if __name__ == '__main__':
    main()
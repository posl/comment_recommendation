def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ret = ''
    for i in range(len(t)):
        if t[i] == '1':
            ret += s1
        elif t[i] == '2':
            ret += s2
        elif t[i] == '3':
            ret += s3
    print(ret)

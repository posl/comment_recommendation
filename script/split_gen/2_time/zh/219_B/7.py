def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = []
    for i in range(len(t)):
        if t[i] == '1':
            result.append(s1)
        elif t[i] == '2':
            result.append(s2)
        elif t[i] == '3':
            result.append(s3)
    print(''.join(result))

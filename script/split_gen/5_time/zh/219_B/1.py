def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ''
    for i in range(len(t)):
        if t[i] == '1':
            result += s1
        elif t[i] == '2':
            result += s2
        else:
            result += s3
    print(result)

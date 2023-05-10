def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    output = ''
    for i in range(len(t)):
        if t[i] == '1':
            output += s1
        elif t[i] == '2':
            output += s2
        elif t[i] == '3':
            output += s3
    print(output)

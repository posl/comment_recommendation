def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ''
    for i in t:
        if i == '1':
            result += s1
        elif i == '2':
            result += s2
        elif i == '3':
            result += s3
    print(result)

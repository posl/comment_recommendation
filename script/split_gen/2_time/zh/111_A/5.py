def main():
    n = input()
    s = ""
    for i in n:
        if i == '1':
            s += '9'
        elif i == '9':
            s += '1'
    print(s)

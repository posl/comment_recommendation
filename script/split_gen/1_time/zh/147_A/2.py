def main():
    a = input()
    b = a.split()
    c = int(b[0]) + int(b[1]) + int(b[2])
    if c >= 22:
        print('bust')
    else:
        print('win')

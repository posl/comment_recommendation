def main():
    a,b,c = map(int,input().split())
    if pow(a,c) < pow(b,c):
        print('<')
    elif pow(a,c) > pow(b,c):
        print('>')
    else:
        print('=')

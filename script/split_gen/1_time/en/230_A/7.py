def main():
    n = int(input())
    if n <= 21:
        print('AGC'+str(100+n)[1:])
    else:
        print('AGC'+str(100+n+1)[1:])

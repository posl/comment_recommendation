def main():
    n = int(input())
    if n < 10:
        print('AGC00'+str(n))
    elif n < 100:
        print('AGC0'+str(n))
    else:
        print('AGC'+str(n))

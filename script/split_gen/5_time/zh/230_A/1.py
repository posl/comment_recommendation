def main():
    n = int(input())
    if n >= 1 and n <= 9:
        print('AGC00'+str(n))
    elif n >= 10 and n <= 99:
        print('AGC0'+str(n))
    else:
        print('AGC'+str(n))

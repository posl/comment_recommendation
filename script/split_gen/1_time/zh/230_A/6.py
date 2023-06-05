def main():
    N = input()
    if int(N) < 10:
        N = '00' + N
    elif int(N) < 100:
        N = '0' + N
    else:
        N = N
    print('AGC' + N)

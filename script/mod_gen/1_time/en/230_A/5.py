def main():
    N = int(input())
    if N < 10:
        print("AGC00"+str(N))
    elif N >= 10 and N < 100:
        print("AGC0"+str(N))
    else:
        print("AGC"+str(N))

if __name__ == '__main__':
    main()
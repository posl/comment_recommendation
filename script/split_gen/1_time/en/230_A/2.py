def main():
    N = int(input())
    if N < 10:
        print("AGC00"+str(N))
    elif N < 100:
        print("AGC0"+str(N))
    else:
        print("AGC"+str(N))

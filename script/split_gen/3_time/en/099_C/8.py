def main():
    N = int(input())
    #print(N)
    #print(type(N))
    #print(N%6)
    #print(N%9)
    if N%6 == 0:
        print(N//6)
    elif N%9 == 0:
        print(N//9)
    else:
        print(N//6+1)

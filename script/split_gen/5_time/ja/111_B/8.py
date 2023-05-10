def main():
    N = int(input())
    #print(N)
    #print(type(N))
    #print(N % 111)
    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1) * 111)
    return

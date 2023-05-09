def main():
    #input
    K = int(input())
    A, B = map(int, input().split())
    #compute
    for i in range(A, B+1):
        if i%K == 0:
            print("OK")
            break
    else:
        print("NG")

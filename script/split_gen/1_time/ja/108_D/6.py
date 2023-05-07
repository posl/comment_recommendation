def main():
    L = int(input())
    if L % 2 == 0:
        print(L//2+1)
        for i in range(L//2):
            print(i+1,i+2)
        print(L//2+1,L)
    else:
        print((L+1)//2)
        for i in range((L+1)//2-1):
            print(i+1,i+2)
        print((L+1)//2,L)

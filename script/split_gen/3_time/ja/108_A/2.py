def main():
    K = int(input())
    if K % 2 == 0:
        print((K//2)**2)
    else:
        print(((K-1)//2)*((K+1)//2))

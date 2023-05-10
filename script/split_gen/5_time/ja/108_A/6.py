def main():
    K = int(input())
    if K % 2 == 0:
        print(int((K/2)**2))
    else:
        print(int((K//2)*(K//2 + 1)))

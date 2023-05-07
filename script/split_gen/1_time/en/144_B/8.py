def main():
    N = int(input())
    if N == 1:
        print('No')
    else:
        for i in range(1, 10):
            if N % i == 0 and N // i <= 9:
                print('Yes')
                break
        else:
            print('No')

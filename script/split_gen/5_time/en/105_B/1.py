def main():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0 or n % 11 == 0:
        print('Yes')
        return
    for i in range(1, n):
        for j in range(1, n):
            if i * 4 + j * 7 == n:
                print('Yes')
                return
    print('No')

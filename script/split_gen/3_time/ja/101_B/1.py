def main():
    n = int(input())
    sum = 0
    for i in str(n):
        sum += int(i)
    if n % sum == 0:
        print('Yes')
    else:
        print('No')

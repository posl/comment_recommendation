def main():
    n = int(input())
    count = 0
    for i in range(n):
        if input() == 'For':
            count += 1
    if count > n/2:
        print('Yes')
    else:
        print('No')

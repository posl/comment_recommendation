def main():
    n = int(input())
    for_count = 0
    for i in range(n):
        if input() == 'For':
            for_count += 1
    if for_count > n//2:
        print('Yes')
    else:
        print('No')

def main():
    n = int(input())
    count = 0
    for i in range(3, n+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    print(count)

def main():
    K = int(input())
    A, B = map(int, input().split())
    if B // K >= A // K:
        print('OK')
    else:
        print('NG')

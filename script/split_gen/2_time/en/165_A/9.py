def main():
    # Get the input
    k = int(input())
    a, b = map(int, input().split())
    # Check the condition
    if a % k == 0 or b % k == 0 or (a // k + 1) * k <= b:
        print('OK')
    else:
        print('NG')

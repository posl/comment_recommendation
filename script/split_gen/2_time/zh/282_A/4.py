def main():
    K = int(input())
    print(''.join([chr(x) for x in range(ord('A'), ord('A') + K)]))

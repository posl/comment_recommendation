def main():
    n = int(input())
    if n > 42:
        print(f'AGC{str(n+1).zfill(3)}')
    else:
        print(f'AGC{str(n).zfill(3)}')

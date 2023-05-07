def main():
    L = int(input())
    if L == 12:
        print(1)
    else:
        print((L-12)*2**((L-13)//2))

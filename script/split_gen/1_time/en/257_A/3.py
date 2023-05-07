def main():
    n, x = map(int, input().split())
    for i in range(1, n+1):
        if x <= 26*i:
            print(chr(64+x-26*(i-1)))
            return
        else:
            x -= 26*i

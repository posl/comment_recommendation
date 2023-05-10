def main():
    h = int(input())
    cnt = 0
    while h > 0:
        cnt += 1
        h = h // 2
    print(2**cnt-1)

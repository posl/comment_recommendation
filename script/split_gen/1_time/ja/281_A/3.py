def main():
    n = int(input())
    if n < 1 or n > 100:
        print('制約違反')
        return
    for i in range(n, -1, -1):
        print(i)

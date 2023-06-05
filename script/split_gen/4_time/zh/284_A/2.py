def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        print(s[-i-1])

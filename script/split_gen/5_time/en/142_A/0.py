def main():
    n = int(input())
    result = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            result += 1
    print(result/n)

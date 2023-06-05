def main():
    a, b, t = map(int, input().split())
    result = 0
    for i in range(1, t + 1):
        if i % a == 0:
            result += b
    print(result)

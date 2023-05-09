def main():
    n = int(input())
    result = 0
    for a in range(1, n):
        for b in range(1, n):
            result += (n - a * b) // a
    print(result)

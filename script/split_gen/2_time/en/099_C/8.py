def main():
    N = int(input())
    result = 0
    while N > 0:
        result += 1
        for i in range(6, -1, -1):
            if N - 6**i >= 0:
                N -= 6**i
                break
            elif N - 9**i >= 0:
                N -= 9**i
                break
    print(result)

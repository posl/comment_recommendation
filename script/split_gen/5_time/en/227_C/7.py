def main():
    N = int(input())
    result = 0
    for a in range(1, N + 1):
        for b in range(a, N + 1):
            ab = a * b
            if ab > N:
                break
            for c in range(b, N + 1):
                abc = ab * c
                if abc > N:
                    break
                else:
                    result += 1
    print(result)

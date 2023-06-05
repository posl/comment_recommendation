def main():
    N = int(input())
    count = 0
    for a in range(1, int(N ** (1/3)) + 1):
        for b in range(a, int(N ** (1/3)) + 1):
            if a * b * (a + b) > N:
                break
            for c in range(b, int(N ** (1/3)) + 1):
                if a * b * c > N:
                    break
                count += 1
    print(count)

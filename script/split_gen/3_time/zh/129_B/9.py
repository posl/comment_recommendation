def main():
    n = int(input())
    weights = [int(x) for x in input().split()]
    weights.sort()
    sum = 0
    for i in range(n):
        sum += weights[i]
    half = sum / 2
    sum1 = 0
    for i in range(n):
        sum1 += weights[i]
        if sum1 >= half:
            if sum1 - half < half - sum1 + weights[i]:
                print(int(sum1 - half) * 2)
            else:
                print(int(half - sum1 + weights[i]) * 2)
            break

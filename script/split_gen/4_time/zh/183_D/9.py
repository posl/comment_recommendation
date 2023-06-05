def main():
    n, w = map(int, input().split())
    water = [0] * 200001
    for i in range(n):
        s, t, p = map(int, input().split())
        water[s] += p
        water[t] -= p
    for i in range(200000):
        water[i + 1] += water[i]
        if water[i] > w:
            print("No")
            return
    print("Yes")

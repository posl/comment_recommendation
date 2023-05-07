def main():
    L = int(input())
    if L % 3 == 0:
        print((L / 3) ** 3)
    elif L % 3 == 1:
        print((L // 3 + 1) * (L // 3) * (L // 3))
    else:
        print((L // 3 + 1) * (L // 3 + 1) * (L // 3))

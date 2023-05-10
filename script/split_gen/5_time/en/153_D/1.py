def main():
    H = int(input())
    count = 1
    while H > 1:
        H = H // 2
        count = count * 2
    print(count * 2 - 1)

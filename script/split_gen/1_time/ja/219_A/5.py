def main():
    x = int(input())
    if x >= 90:
        print("expert")
    else:
        print(40 * ((x // 40) + 1) - x)

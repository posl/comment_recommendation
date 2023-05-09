def main():
    x = int(input())
    count = 0
    while x > 100:
        x = int(x * 1.01)
        count += 1
    print(count)

def main():
    X = int(input())
    happiness = (X // 500) * 1000
    happiness += (X % 500) // 5 * 5
    print(happiness)

def main():
    x = int(input())
    result = 0
    deposit = 100
    while deposit < x:
        deposit += deposit // 100
        result += 1
    print(result)

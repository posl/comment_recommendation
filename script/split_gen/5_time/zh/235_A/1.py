def main():
    abc = int(input())
    bca = abc % 10 * 100 + abc // 10 % 10 * 10 + abc // 100
    cab = abc // 100 * 100 + abc % 10 * 10 + abc // 10 % 10
    print(abc + bca + cab)

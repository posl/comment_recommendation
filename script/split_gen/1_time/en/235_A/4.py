def main():
    #input
    abc = int(input())
    #compute
    bca = abc % 100 * 10 + abc // 100
    cab = abc % 10 * 100 + abc // 10
    #output
    print(abc + bca + cab)

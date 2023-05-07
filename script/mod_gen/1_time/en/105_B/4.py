def buy_cakes_and_doughnuts(n):
    for i in range(n//4+1):
        for j in range(n//7+1):
            if 4*i+7*j==n:
                return "Yes"
    return "No"

if __name__ == '__main__':
    buy_cakes_and_doughnuts()
def main():
    Y = int(input())
    #Y = 2022
    #Y = 2023
    #Y = 3000
    
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + (4 - Y % 4))

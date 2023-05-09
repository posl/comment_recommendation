def main():
    S = input()
    T = input()
    S = S.replace('a','1').replace('b','2').replace('c','3')
    T = T.replace('a','1').replace('b','2').replace('c','3')
    print('Yes' if S == T else 'No')
main()

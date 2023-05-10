def main():
    a, b, c = map(int, input().split())
    print((a*100+b*100+c*100-300)/(a+b+c))
main()
# %%

if __name__ == '__main__':
    main()
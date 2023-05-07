def main():
    a,b,c = map(int, input().split())
    print((a*b*b*100 + a*c*c*100 + b*c*c*100)/(a*b*c*100 - a*b*b*100 - a*c*c*100 - b*c*c*100))
main()

if __name__ == '__main__':
    main()
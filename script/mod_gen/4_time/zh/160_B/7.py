def main():
    x = int(input())
    y = x//500
    z = x%500//5
    print(y*1000+z*5)

if __name__ == '__main__':
    main()
def main():
    x = int(input())
    ans = (x//500)*1000
    x = x%500
    ans += (x//5)*5
    print(ans)

if __name__ == '__main__':
    main()
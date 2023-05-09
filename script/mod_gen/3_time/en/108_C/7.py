def main():
    N, K = map(int, input().split())
    print(((N//K)**3)+((N//K)**2)*((N-N//K)**2)*2+((N//K)**2)*((N//K)**2)*2+((N-N//K)**2)*((N-N//K)**2)*2)

if __name__ == '__main__':
    main()
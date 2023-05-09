def main():
    K = int(input())
    print('{0:02}:{1:02}'.format((21+K//60)%24,K%60))

if __name__ == '__main__':
    main()
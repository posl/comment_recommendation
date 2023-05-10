def main():
    K = int(input())
    print('{:02d}:{:02d}'.format((K+120)//60, (K+120)%60))

if __name__ == '__main__':
    main()
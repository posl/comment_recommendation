def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print('{:02d}:{:02d}'.format(H+21, M))

if __name__ == '__main__':
    main()
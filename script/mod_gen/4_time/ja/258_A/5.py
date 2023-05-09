def main():
    K = int(input())
    h = K // 60
    m = K % 60
    print(str(21+h).rjust(2,'0') + ':' + str(m).rjust(2,'0'))

if __name__ == '__main__':
    main()
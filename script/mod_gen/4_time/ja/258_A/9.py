def main():
    import sys
    #input = sys.stdin.readline
    #print = sys.stdout.write
    #K = int(input())
    K = int(input())
    H = K // 60
    M = K % 60
    print("%02d:%02d" % (H,M))

if __name__ == '__main__':
    main()
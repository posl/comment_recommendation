def main():
    N = int(input())
    
    # 1円引き出し回数
    count = N
    
    # 6円引き出し回数
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if 6**i + 6**j + 6**k == N:
                    count = min(count, i + j + k)
                    
    # 9円引き出し回数
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if 9**i + 9**j + 9**k == N:
                    count = min(count, i + j + k)
                    
    print(count)

if __name__ == '__main__':
    main()
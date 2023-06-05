def main():
    antennas = []
    # 读取输入
    for i in range(6):
        antennas.append(int(input()))
    # print(antennas)
    # 处理
    for i in range(5):
        for j in range(i + 1, 5):
            if antennas[j] - antennas[i] > antennas[5]:
                print(":(")
                return
    print("Yay!")

if __name__ == '__main__':
    main()
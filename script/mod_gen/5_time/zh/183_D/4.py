def main():
    # 读入数据
    data = []
    with open("problems183_d.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())
    print(data)
    # 处理数据
    # 1. 人数
    n = int(data[0].split(" ")[0])
    # 2. 热水器每分钟提供热水的升数
    w = int(data[0].split(" ")[1])
    # 3. 人员计划
    people = []
    for line in data[1:]:
        people.append([int(x) for x in line.split(" ")])
    # 4. 按照开始时间对人员计划进行排序
    people.sort(key=lambda x: x[0])
    # 5. 从第一位开始计算，如果热水器提供的热水量大于等于计划使用的热水量，那么可以按照计划进行供热，否则不能
    for i in range(n):
        if w < people[i][2]:
            print("No")
            return
        w += people[i][2]
    print("Yes")

if __name__ == '__main__':
    main()
def getCityCount(cityCount, citys):
    for i in range(1, cityCount + 1):
        count = 0
        citys = sorted(citys, key=lambda x: x[0])
        for j in range(len(citys)):
            if i in citys[j]:
                count += 1
                citys[j].remove(i)
        print(count, end=' ')
        for j in range(count):
            print(citys[j][0], end=' ')
        print()

if __name__ == '__main__':
    getCityCount()
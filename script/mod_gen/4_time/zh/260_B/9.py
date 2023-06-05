def input_data():
    data = []
    for i in range(3):
        data.append(input())
    data.append(input().split())
    data.append(input().split())
    return data

if __name__ == '__main__':
    input_data()
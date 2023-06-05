def main():
    # 读取输入
    # 读取输入
    line = input()
    line = line.split()
    #print(line)
    a = int(line[0])
    b = int(line[1])
    #print(a,b)
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

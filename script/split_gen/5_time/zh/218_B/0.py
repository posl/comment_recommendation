def main():
    line = input()
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    for i in range(len(line)):
        line[i] -= 1
    output = [0 for i in range(len(line))]
    for i in range(len(line)):
        output[line[i]] = chr(ord('a') + i)
    print(''.join(output))

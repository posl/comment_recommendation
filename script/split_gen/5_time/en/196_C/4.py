def main():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                result += 1
    print(result)

def main():
    input_list = [int(i) for i in input().split()]
    for i in range(5):
        if input_list[i] == 0:
            print(i+1)
            break

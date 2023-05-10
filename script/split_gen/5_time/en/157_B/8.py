def main():
    # Take input from stdin
    input_list = []
    for i in range(3):
        input_list.append(list(map(int, input().split())))
    N = int(input())
    for i in range(N):
        b = int(input())
        # Check if b is in input_list
        for j in range(3):
            for k in range(3):
                if input_list[j][k] == b:
                    input_list[j][k] = 0
    # Check if we have a bingo
    if input_list[0][0] == 0 and input_list[1][1] == 0 and input_list[2][2] == 0:
        print("Yes")
    elif input_list[0][2] == 0 and input_list[1][1] == 0 and input_list[2][0] == 0:
        print("Yes")
    elif input_list[0][0] == 0 and input_list[0][1] == 0 and input_list[0][2] == 0:
        print("Yes")
    elif input_list[1][0] == 0 and input_list[1][1] == 0 and input_list[1][2] == 0:
        print("Yes")
    elif input_list[2][0] == 0 and input_list[2][1] == 0 and input_list[2][2] == 0:
        print("Yes")
    elif input_list[0][0] == 0 and input_list[1][0] == 0 and input_list[2][0] == 0:
        print("Yes")
    elif input_list[0][1] == 0 and input_list[1][1] == 0 and input_list[2][1] == 0:
        print("Yes")
    elif input_list[0][2] == 0 and input_list[1][2] == 0 and input_list[2][2] == 0:
        print("Yes")
    else:
        print("No")

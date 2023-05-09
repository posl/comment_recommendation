def check_result(result):
    for i in range(len(result)):
        for j in range(len(result)):
            if i != j:
                if result[i][j] == 'W':
                    if result[j][i] != 'L':
                        print("incorrect")
                        return
                elif result[i][j] == 'L':
                    if result[j][i] != 'W':
                        print("incorrect")
                        return
                elif result[i][j] == 'D':
                    if result[j][i] != 'D':
                        print("incorrect")
                        return
    print("correct")

if __name__ == '__main__':
    check_result()
def get_answer(N):
    answer = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if int(str(i)[-1]) == int(str(j)[0]) and int(str(i)[0]) == int(str(j)[-1]):
                answer += 1
    return answer

if __name__ == '__main__':
    get_answer()
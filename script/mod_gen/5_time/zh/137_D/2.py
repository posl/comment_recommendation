def max_reward(n, m, work):
    work.sort(key=lambda x: x[0])
    reward = 0
    for i in range(n):
        if work[i][0] <= m:
            m += work[i][1]
            reward += work[i][1]
        else:
            break
    return reward

if __name__ == '__main__':
    max_reward()
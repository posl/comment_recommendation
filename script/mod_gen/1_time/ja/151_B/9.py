def is_achieved_goal(score_list, score, goal):
    score_list.append(score)
    score_list.sort()
    score_list.reverse()
    score_list.pop()
    score_list.reverse()
    if sum(score_list) / len(score_list) >= goal:
        return True
    else:
        return False

if __name__ == '__main__':
    is_achieved_goal()
import os

def rename(path):
    # ABC099 ~ ABC287
    problem_l = os.listdir(path)
    problem_l = sorted(problem_l)
    #print(problem_l)
    if '.DS_Store' in problem_l:
        problem_l.remove('.DS_Store')
    for problem in problem_l:
        for difficulty in ['A', 'B', 'C', 'D']:
            for f in ['in', 'out']:
                each_test_case_l = os.listdir(path + problem + '/' + difficulty + '/' + f + '/')
                each_test_case_l = sorted(each_test_case_l)
                if '.DS_Store' in each_test_case_l:
                    each_test_case_l.remove('.DS_Store')
                for each_test_case in each_test_case_l:
                    os.rename(path + problem + '/' + difficulty + '/' + f + '/' + each_test_case, path + problem + '/' + difficulty + '/' + f + '/' + each_test_case.split('.')[0] + '.txt')
        print(problem)
    
def check(path):
    problem_l = sorted(os.listdir(path))
    if '.DS_Store' in problem_l:
        problem_l.remove('.DS_Store')
    for problem in problem_l:
        for difficulty in ['A', 'B', 'C', 'D']:
            for f in ['in', 'out']:
                each_test_case_l = sorted(os.listdir(path + problem + '/' + difficulty + '/' + f + '/'))
                if '.DS_Store' in each_test_case_l:
                    each_test_case_l.remove('.DS_Store')
                for each_test_case in each_test_case_l:
                    if each_test_case.split('.')[1] != 'txt':
                        print(problem + '/' + difficulty + '/' + f + '/' + each_test_case)
        print(problem)

if __name__ == '__main__':
    path = '/Users/keikoyanagi/Desktop/comment_recommendation/test_case/'
    #rename(path)
    check(path)
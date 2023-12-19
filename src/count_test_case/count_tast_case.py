import os

class CountTestCase:
    def __init__(self, Base_path):
        self.base_path = '{0}/test_case/'.format(Base_path)
        self.each_path_l = os.listdir(self.base_path)
        if '.DS_Store' in self.each_path_l:
            self.each_path_l.remove('.DS_Store')
        self.each_test_case_l = []
        self.each_difficulty_dict = {}

    def main(self):
        for each_difficulty in ['A', 'B', 'C', 'D']:
            for each_path in self.each_path_l:
                self.count_test_case(each_path, each_difficulty)
            self.each_test_case_l.sort()
            self.each_difficulty_dict[each_difficulty] = sum(self.each_test_case_l) / len(self.each_test_case_l)
            self.each_test_case_l = []
        return self.each_difficulty_dict
        

    def count_test_case(self, Each_path, Difficulty):
        each_path = '{0}{1}/{2}/in/'.format(self.base_path, Each_path, Difficulty)
        each_test_case = os.listdir(each_path)
        self.each_test_case_l.append(len(each_test_case))
        return
    
if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    count_test_case = CountTestCase(base_path)
    print(count_test_case.main())
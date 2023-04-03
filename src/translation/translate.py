import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('DeepL_API_KEY')

class translation():
    def __init__(self, file):
        self.file = file

    def translate(self):
        with open('../../data/en/{}'.format(self.file), 'r') as f:
            self.source_file_l = f.read()
            #print(self.source_file)
        
        url = 'https://api.deepl.com/v2/translate'
        params = {
            'auth_key': API_KEY,
            'text': self.source_file_l,
            'source_lang': 'EN',
            'target_lang': 'ZH'
        }

        request = requests.post(url, data=params)
        result = request.json()
        #print(result)
        
        with open('../../data/zh/{}'.format(self.file), 'w') as f:
            f.write(result['translations'][0]['text'])
        
        
        



if __name__ == '__main__':
    path = '../../data/en/'
    files = os.listdir(path)
    files = sorted(files)
    for file in files:
        print(file)
        t = translation(file)
        t.translate()
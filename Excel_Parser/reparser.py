"""Парсинг XML и пуш в таблицу в соответствии с ключами включая условия"""

import itertools
import pandas as pd



df = pd.read_excel(r'C:\Users\Iclub\Desktop\parserTest.xls', sheet_name='Sheet1')
var1 = df['first (A1)'].tolist()

for i in range(len(var1)):
 words = var1[i].split()
 

 def get_permutations(words):
     res = ''
     for item in itertools.permutations(words):
         res += ' '.join(item) + ', '
     return res


 print(get_permutations(words))


from BeautifulSoup import BeautifulStoneSoup as Soup

soup = Soup(open(filename))
for tag in soup.findAll('ns1:name'):
    print tag.find('ns1:familyname').text
    print tag.find('ns1:fullname').text
    print tag.find('ns1:givenname').text
for tag in soup.findAll('ns1:organization'):
    print tag.find('ns1:orgtitle').text
    print tag.find('ns1:orgdepartment').text
    print tag.find('ns1:orgname').text
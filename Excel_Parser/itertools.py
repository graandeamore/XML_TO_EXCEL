"""Напишите функцию, которая принимает массив элементов и возвращает все возможные комбинации этих элементов."""

import itertools
import pandas as pd
df = pd.read_excel(r'C:\Users\Iclub\Desktop\Прайс KREONOPT - Июль.xls', sheet_name='Пробники')
var1 = df['first (A1)'].tolist()
for i in range(len(var1)):
 words = var1[i].split()
 def get_permutations(words):
     res = ''
     for item in itertools.permutations(words):
         res += ' '.join(item) + ', '
     return res
 if len(words) < 5:
     print(i, get_permutations(words))
 else:
     print(i, 'High')


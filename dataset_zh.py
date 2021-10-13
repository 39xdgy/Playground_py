import efaqa_corpus_zh as efdata

l = list(efdata.load())
'''
for key in l[0].keys():
    print(f'{key}: {l[0][key]}')

'''

for data in l:
    print(data['title'])
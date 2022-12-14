import re
import pandas as pd


def get_names(sample):
    a1 = sample.replace(' ', '').replace('=%s', '').replace('=%f', '').replace('=%d', '')
    return a1.split(',')


def choose_lines(lines, regexp):  # choose correct lines
    res = []
    for i in range(len(sentences)):
        regexp = re.compile(regexp)
        result = regexp.search(sentences[i])
        if result:
            res.append(sentences[i])
    return res  # returns list of correct lines


def regexp_translate(regexp):
    return regexp.replace('%d','\s*[+-]?[0-9]+').replace('%s', '\s*\w+').replace('%f', '\s*[+-]?[0-9]+\.[0-9]+')


def get_params(lines, names):
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' ', '')
        for j in names:
            lines[i] = lines[i].replace(j + '=', '')
    return lines


sentences = []
sentences.append('x = 33, y = -18.22, z = cdcd, ppp = abc')
sentences.append('one more line')
sentences.append('x = 1, y = 1.16, z = x, ppp = shit')
sentences.append('line')
sentences.append('line')
sentences.append('line')
sentences.append('x = 343, y = 2.2, z = 999AAA99Zh, ppp = cda')

sample = 'x = %d, y = %f, z = %s, ppp = %s'
names = get_names(sample)

regexp = regexp_translate(sample)

lines = choose_lines(sentences, regexp)

params = get_params(lines, names)
df = pd.DataFrame(columns=names, index=range(0, len(lines)))
for i in range(len(params)):
  targets=params[i].split(',')
  for j in range(len(names)):
    df[names[j]][i]=targets[j]


print(df)
df.to_csv('result.csv')

import requests

from bs4 import BeautifulSoup

url = str(input())
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
site_content = soup.find_all(['a'])
answer = list()
# site_content = soup.getText
for tag in site_content:
    topic = str(tag)
    topic = topic.replace('\n', '')
    _tag = str(tag).replace('\n', '')
    if 'href' not in _tag:
        continue
    if '/redirect-' in _tag:
        continue
    if '/newsletter' in _tag:
        continue
    if '<img' in _tag:
        continue
    # if '/health-topics/' not in _tag:
    #     continue
    # print(topic)
    delete_tag = False
    tag_open = 0
    for symbol_id in range(0, len(_tag)):
        if _tag[symbol_id] == '<':
            # print('works' + str(symbol_id))
            tag_open = symbol_id
            delete_tag = True
        if _tag[symbol_id] == '>':
            if delete_tag:
                delete_tag = False
                topic = topic.replace(_tag[tag_open:symbol_id + 1], '')
                # print('works')
    answer.append(topic)

# print(answer)
# answer = [x for x in answer if ' ' in x]
# print(answer)
answer = [x for x in answer if x.startswith('S')]
answer = [x for x in answer if len(x) > 1]
# answer = [x for x in answer if '»' not in x]
# _set = set()
# for x in answer:
#     _set.add(x)
# answer.clear()
# for x in _set:
#     answer.append(x)
print(answer)

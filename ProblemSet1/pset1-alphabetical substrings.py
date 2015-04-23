s = 'lfgskypntweamtwyhrd'
word = s[0]

for i in range(len(s)-1):
    if s[i+1] >=  s[i]:
        word += s[i+1]
    else:
        word += ' ' + s[i+1]

final_list = word.split()
biggest_sorted_word = ''

for words in final_list:
    if len(biggest_sorted_word) < len(words):
        biggest_sorted_word = words

print biggest_sorted_word

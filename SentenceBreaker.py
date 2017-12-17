#python sentence tokenizer - by Chaitra

import codecs
import nltk
nltk.download('punkt')
import nltk.data

print('')
print('')
print('')
print('loading dependencies completed..')
print('----------------------------------------')
print('')
print('')
print('')

languages_ = ['czech','danish','dutch','english','estonian','finnish','french','german','greek','italian','norwegian','polish','portuguese','slovene','spanish','swedish','turkish']

lang_count = 0
selected_language = ''
input_language = ''

print('Python Sentence Breaker - v1.0 - By Chaitra Dangat')
print('')
print('Language-List')
print('-----------------------------------------------')
for language_ in languages_:
	lang_count += 1
	print(str(lang_count) + '.' + language_)
print('--------------------------------------------------')

input_language = input('Select A Language:')

try: 
    if int(input_language) >= len(languages_):
     print('invalid selection!')
     quit()
    else:
     selected_language = languages_[int(input_language)-1]
     print('')
     print('language selected-->'+selected_language)
     print('')
except ValueError:
    quit()

tokenizer = nltk.data.load('tokenizers/punkt/'+selected_language+'.pickle')
print('tokenizers/punkt/'+selected_language+'.pickle')
#input file path
input_file = input('Enter the text file path :')

#output folder path
output_folder = input('Enter the output folder path :')
output_file = output_folder + '\\' + 'output-tokenized.txt'

result_output = []
output_ = open(output_file, 'w', encoding='utf-8')

print('Reading Input File...')

input_ = codecs.open(input_file, encoding='utf-8')

combined_line = ''

i = 0
for line in input_:
    i += 1
    if i%100 == 0:
     print('lines processed-->' + str(i))
    else:
     pass
    if i%1000 == 0:
            combined_line += ' ' + line
            result = tokenizer.tokenize(combined_line)
            for op in result:
               output_.write(op)
            combined_line = ''
    else:
            combined_line += ' ' + line


if combined_line != '':
    result = tokenizer.tokenize(combined_line)
    for op in result:
      output_.write(op)
else:
  pass

print('Processing Completed')
input('')
input_.close()
output_.close()
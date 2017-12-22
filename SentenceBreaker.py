#python sentence tokenizer - by Chaitra
print('')

print('loading dependencies...')
print('-----------------------------------------------------------------------')
import codecs
import nltk
nltk.download('punkt')
import nltk.data
print('-----------------------------------------------------------------------')
print('loading dependencies completed')
print('')
print('')


languages_ = ['czech','danish','dutch','english','estonian','finnish','french','german','greek','italian','norwegian','polish','portuguese','slovene','spanish','swedish','turkish']

lang_count = 0
selected_language = ''
input_language = ''
custom_required = False
tokenizer = ''

print('Python Sentence Breaker - v1.1 - By Chaitra Dangat')
print('')
print('Language-List')
print('-----------------------------------------------------------------------')
for language_ in languages_:
	lang_count += 1
	print(str(lang_count) + '.' + language_)
print('-----------------------------------------------------------------------')

input_language = input('Select A Language:')

try: 
    if int(input_language) > len(languages_):
     print('invalid selection!')
     quit()
    else:
     selected_language = languages_[int(input_language)-1]
     print('language selected: '+selected_language)
     print('')
except ValueError:
    print('invalid selection!')
    quit()

print('Setting-File')
print('-----------------------------------------------------------------------')
try:
 custom_setting_file = input('Enter custom setting file path(optional):')
 custom_setting_file = custom_setting_file.replace("\\", "/")
 tokenizer = nltk.data.load('file:' + custom_setting_file)
 print('custom settings loaded successfully')
 custom_required = True
except:
 print('error loading custom setting file')
 print('loading default setting file..')

if custom_required == False:
 try:
  #print selected pickle file path 
  print('')
  print('settings file path: ' +nltk.data.find('tokenizers/punkt/'+selected_language+'.pickle'))
  #load pickle file from nltk data
  tokenizer = nltk.data.load('tokenizers/punkt/'+selected_language+'.pickle')
  print('settings loaded successfully...')
 except:
  print('***********************************************************************')
  print('Error loading settings file: \"' + selected_language+'.pickle' + '\"')
  print('Please check \"' + selected_language +'.pickle' + '\" file exists in:')
  for path_ in nltk.data.path:
   print(path_ + '\\tokenizers\\punkt')
  print('***********************************************************************')
  quit() 
else:
 pass
print('-----------------------------------------------------------------------')
 
print('')
#input file path
input_file = input('Enter the text file path :')

#output folder path
output_folder = input('Enter the output folder path :')
output_file = output_folder + '\\' + 'output-tokenized.txt'

result_output = []
output_ = open(output_file, 'w', encoding='utf-8')

print('Reading Input File...')

input_ = codecs.open(input_file, encoding='iso-8859-1')

combined_line = ''

i = 0
for line in input_:
    i += 1
    if i%100 == 0:
     print('lines processed-->' + str(i))
    else:
     pass
    #if i%1000 == 0:
    #combined_line += ' ' + line
    #result = tokenizer.tokenize(combined_line)
    try:
     result = tokenizer.tokenize(line)
     print(result)
     for op in result:
      output_.write(op)
      output_.write('\n')
    except:
     pass
    #combined_line = ''
    #else:
    #combined_line += ' ' + line

#if combined_line != '':
    #result = tokenizer.tokenize(combined_line)
    #for op in result:
      #output_.write(op)
#else:
  #pass

print('Processing Completed')
input('')
input_.close()
output_.close()
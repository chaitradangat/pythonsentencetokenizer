#python sentence tokenizer - by Chaitra

tokenizer = ''
selected_language = ''

def loadNltkdependdencies():
 print('')
 print('loading dependencies...') 
 print('-----------------------------------------------------------------------')
 nltk.download('punkt')
 print('-----------------------------------------------------------------------')
 print('loading dependencies completed')
 print('')
 print('') 

def loadLanguageList():
 #variables
 lang_count = 0 
 input_language = ''
 selected_language_ = ''
 #language list
 languages_ = ['czech','danish','dutch','english','estonian','finnish','french','german',
              'greek','italian','norwegian','polish','portuguese','slovene','spanish','swedish','turkish']  
 print('Language-List')
 print('-----------------------------------------------------------------------')
 
 for language_ in languages_:
  lang_count += 1
  print(str(lang_count) + '.' + language_)
 print('-----------------------------------------------------------------------')
 input_language = input('Select A Language:')

 try:
  if int(input_language) > len(languages_):
   pass
  else:
   selected_language_ = languages_[int(input_language)-1]
 except ValueError:
  pass
 return selected_language_
 
def DisplayProgramHeader():
 print('Python Sentence Breaker - v1.1 - By Chaitra Dangat')
 print('')

def LoadSettingFile(selected_language_):
 tokenizer_ = ''
 custom_required_ = False
 print('Setting-File')
 print('-----------------------------------------------------------------------')
 try:
  custom_setting_file = input('Enter custom setting file path(optional):')
  custom_setting_file = custom_setting_file.replace("\\", "/")
  tokenizer_ = nltk.data.load('file:' + custom_setting_file)
  print('custom settings loaded successfully')
  custom_required_ = True
 except:
  print('error loading custom setting file')
  print('loading default setting file..')
 if custom_required_ == False:
  try:
   #print selected pickle file path 
   print('')
   print('settings file path: ' +nltk.data.find('tokenizers/punkt/'+selected_language_+'.pickle'))
   #load pickle file from nltk data
   tokenizer_ = nltk.data.load('tokenizers/punkt/'+selected_language_+'.pickle')
   print('settings loaded successfully...')
  except:
   print('***********************************************************************')
   print('Error loading settings file: \"' + selected_language_+'.pickle' + '\"')
   print('Please check \"' + selected_language_ +'.pickle' + '\" file exists in:')
   for path_ in nltk.data.path:
    print(path_ + '\\tokenizers\\punkt')
   print('***********************************************************************')
 else:
  pass
 return tokenizer_
 print('-----------------------------------------------------------------------')

def ProcessFile(input_file_,output_folder_,tokenizer_):
 output_file = output_folder_ + '\\' + 'output-tokenized-new.txt'
 output_ = open(output_file, 'w', encoding='iso-8859-1')

 print('Reading Input File...')
 input_ = codecs.open(input_file_, encoding='iso-8859-1')

 i = 0
 for line in input_:
  i += 1
  if i%100 == 0:
   print('lines processed-->' + str(i))
  else:
   pass
   pass
  try:
   result = tokenizer_.tokenize(line)
   for op in result:
    output_.write(op)
    output_.write('\n')
  except:
   pass
 input_.close()
 output_.close()

import codecs
import nltk
loadNltkdependdencies()
import nltk.data

DisplayProgramHeader()

selected_language = loadLanguageList()
if selected_language != '':
 print('language selected: '+selected_language)
 print('')
else:
 print('invalid selection!')
 quit() 
 
tokenizer = LoadSettingFile(selected_language)
if tokenizer != '':
 pass
else:
 print('Unable to load settings!')
 quit()
 
print('')
#input file path
input_file = input('Enter the text file path :')

#output file path
output_folder = input('Enter the output folder path :')
 
ProcessFile(input_file,output_folder,tokenizer)
 
print('Processing Completed')
input('')
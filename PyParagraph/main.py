import re # import reg. exp. lib 
import os 
#input file name - to be used later for other files in same dir location 

file_name=input("Input File (*.txt):")

# for file location 
input_file = os.path.join("raw_data", file_name)



with open(input_file, 'r') as txtfile:
    data=txtfile.read().replace('\n', "")


word_list=re.split(r'\s*',data)
sent_list=re.findall(r'\.', data)
sent=re.split(r'\.', data)
sent_lent=[len(i) for i in sent]

if sent_lent[-1]==0:
    del sent_lent[-1]

word_count=len(word_list)
sent_count=len(sent_list)

word_lnt=[len(word) for word in word_list] 



print('Paragraph Analysis')
print("-----------------")
print('Approximate Word Count: ' + str(word_count))
print('Approximate Sentence Count: ' + str((sent_count)))
print('Average Letter Count: ' + str(sum(word_lnt)/len(word_lnt)))
print('Average Sentence Length: '+ str(sum(sent_lent)/len(sent_lent)))
print("-----------------")
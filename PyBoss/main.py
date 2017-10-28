# import os and csv lib to load data 
import os
import csv

# State abr to be used later 
from st_abr import us_state_abbrev 

#input file name - to be used later for other files in same dir location 
file_name=input("Input employee file data name:")

# for file location 
emp_file = os.path.join("raw_data", file_name)

edited_file_name=('edited_' + file_name)

# for file location 
emp_file_eidted = os.path.join("edited_data", edited_file_name)

# intiate Revenue and Months lists to stor values   
ID=[]
first_name=[]
last_name=[]
names=[]
DOB=[]
SSN=[]
state=[]
# open the file and loop over the fhd, update Revenue=[] and Months=[]
with open(emp_file, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip csv headers  
    next(csv_reader, None)

    # Loop over fh
    for row in csv_reader:
        ID.append(row[0])
        names.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        state.append(row[4])
        
    
for name in names:
    first_name.append(name.split()[0])
    last_name.append(name.split()[1])
    
DOB2=[]
dob_string=''
for i in DOB:
    dob_string=(i.split(sep='-')[2] + '/' + i.split(sep='-')[1] + '/' + i.split(sep='-')[0])
    DOB2.append(dob_string)
    
    
SSN2=[]
ssn_string=''
for i in SSN:
    ssn_string=('***-**-'+ i.split(sep='-')[2])
    SSN2.append(ssn_string)
    

# State abr to be used later 
from st_abr import us_state_abbrev 

states = []
for i in state:
    states.append(us_state_abbrev[i])
    
    
# Edited data csv output 
col_data=zip(ID, first_name, last_name, DOB2, SSN2, states)
col_titles=['Emp ID','First Name','Last Name','DOB','SSN','State']


#  Open the output file
with open(emp_file_eidted, 'w', newline="") as clean_csv:
    writer = csv.writer(clean_csv)

    # write titles 
    writer.writerow(col_titles)
    
    # Write data from zip file 
    writer.writerows(col_data)
print('Please find file in: ' + emp_file_eidted)
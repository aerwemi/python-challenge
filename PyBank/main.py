# import os and csv lib to load data 
import os
import csv

#input file name - to be used later for other files in same dir location 
file_name=input("Input Revenue file data name:")

# for file location 
Revenue_data = os.path.join("raw_data", file_name)

# intiate Revenue and Months lists to stor values   
Revenue=[]
Months=[]

# open the file and loop over the fhd, update Revenue=[] and Months=[]
with open(Revenue_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip csv headers  
    next(csv_reader, None)

    # Loop over fh
    for row in csv_reader:
        Months.append(row[0]) # Update Months list 
        Revenue.append(int(row[1])) # Update Rev list
        


# work out change data and store it in a list  
val=Revenue[0] # set initial value  
Change=[] # set change values list  
for i in Revenue: # loop over Revenue list to calculate change 
    Diff=i-val
    Change.append(Diff) # update Change 
    val=i



max_index=[i for i, j in enumerate(Change) if j == (max(Change))][0] # index of max Change 
min_index=[i for i, j in enumerate(Change) if j == (min(Change))][0] # index of min Change 


#Data Summary 
#Simple functions to find from list(s)

Total_Months=len(Revenue)
Total_Revenue=sum(Revenue) 

Average_Revenue_Change=((sum(Change))/(len(Change)-1)) # (len(Change) -1 ) to ignore the first month 

Greatest_Increase_Month=Months[max_index] # find the month of max change via index of max in Change 
Greatest_Increase_Change=max(Change)

Greatest_Decrease_Month=Months[min_index] # find the month of min change via index of min in Change 
Greatest_Decrease_Change=min(Change)



# Print out the Summary 
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(Total_Months)) 
print('Total Revenue: $' + str(Total_Revenue))
print('Average Revenue Change: $' + str(Average_Revenue_Change))
print('Greatest Increase in Revenue:' + Greatest_Increase_Month +" $"+ str(Greatest_Increase_Change))
print('Greatest Decrease in Revenue:' + Greatest_Decrease_Month +" $"+ str(Greatest_Decrease_Change))
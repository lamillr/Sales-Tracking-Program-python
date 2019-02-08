#TO DO Add an #8 to the menu to end program and program that feature
#Go through each function in CFInput.py to see if I understand them
#Go through each function in complete program and look at the book again to make sure I understand them


#This demonstrates refactoring a program into functions

#This program reads in 10 sales values and then prints them out
#in the order thy were entered by working through the sales list.

#fetch the input functions

print('This program reads in 10 sales values and then prints them out')
print('\nThen you have the option on how to sort the sales list')
print('\n')

from CFInput import*

sales =[]

def read_sales(no_of_sales):
    '''
    Reads in the sales values and stores them in the sales list.
    No_of_sales gives the number of sales to store.
    '''

#remove all previous sales values
    sales.clear()
#read in 10 sales figures
    for count in range(1,no_of_sales+1):
#assemble a prompt string look up str(count)
        prompt = 'Enter the sales for stand ' + str(count) + ':'
# read a value and append it to sales list
        sales.append(read_int(prompt))
# print a heading
def print_sales():
    '''
    Prints the sales figures on the screen with a heading.
    Each figure is numbered in a sequence.
    '''
    print("Sales Figures")
#initialize the stand counter
    count = 1
#work through the sales figures and print them
    for sales_value in sales:
        print('Sales for stand', count,'are',sales_value)
#advance the stand counter
        count = count + 1

def sort_high_to_low():
    '''
    Print out a list of the sales_value figures sorted high to lowest
    '''
    for sort_pass in range(0,len(sales)):
        done_swap=False
        for count in range(0, len(sales)-1):
            if sales[count]<sales[count + 1]:
                temp=sales[count]
                sales[count]=sales[count+1]
                sales[count+1]=temp
                done_swap=True
            if done_swap==False:
                break
    print_sales()

def sort_low_to_high():
    '''
    Print out a list of the sales_value figures sorted high to lowest
    '''
    for sort_pass in range(0,len(sales)):
        done_swap=False
        for count in range(0,len(sales)-1-sort_pass):
            if sales[count]>sales[count+1]:
                temp=sales[count]
                sales[count]=sales[count+1]
                sales[count+1]=temp
                done_swap=True
        if done_swap==False:
            break
    print_sales()

def highest_and_lowest():
    '''
    Print out the highest and the lowest sales value
    '''
    highest=sales[0]
    lowest=sales[0]
    for sales_value in sales:
        if sales_value>highest:
            highest=sales_value
        if sales_value<lowest:
            lowest=sales_value
    print('The highest is:', highest)
    print('The lowest is:',lowest)

def total_sales():
    '''
    Print out total sales value
    '''
    total=0
    for sales_value in sales:
        total=total+sales_value
    print('Total sales are:', total)

def average_sales():
    '''
    Print out the average sales value
    '''
    total=0
    for sales_value in sales:
        total=total+sales_value
    average_sales=total/len(sales)
    print('Average sales are:', average_sales)

#Complete the Program
#Start by reading in the sales
read_sales(10)

#now get the command from the user
menu='''Coffee sales
1: Print the sales
2: Sort High to Low
3: Sort Low to High
4: Highest and Lowest
5: Total Sales
6: Average Sales
7: Enter figures
8: Stop program


Enter your command: '''

#Now repeatedly read commands and act on them
while True:
    command=read_int_ranged(menu,1,8)
    if command==1:
        print_sales()
    elif command==2:
        sort_high_to_low()
    elif command==3:
        sort_low_to_high()
    elif command==4:
        highest_and_lowest()
    elif command==5:
        total_sales()
    elif command==6:
        average_sales()
    elif command==7:
        read_sales(10)
    elif command==8:
        exit()
   

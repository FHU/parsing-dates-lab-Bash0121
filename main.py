#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    month_list={
        "January" : "01",
        "Febuary" : "02",
        "March" : "03",
        "April" : "04",
        "May" : "05",
        "June" : "06",
        "July" : "07",
        "August" : "08",
        "September" : "09",
        "October" : "10",
        "November" : "11",
        "December" : "12"
    }
    
    for i in month_list.keys():
       if i == month[0]:
         month[0] = i
         return month

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    parse_month()
    joined_string=user_string.join(" ")
    joined_string1=joined_string.replace(" ", "/")
    joined_string2=joined_string1.removed(",")
    return joined_string2

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
   list1=[]
   counter=0
   u_input1=input()
   while counter>0:
    if u_input1==-1:
       counter+=1
    else:
       list1=u_input1.split()
       parse_month(list1)
       print(parse_date())

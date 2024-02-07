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
    
    num=month_list[month]
    return num

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    month_parse=parse_month(user_string[0])
    day=user_string[1]
    day=day.replace(",","")
    if int(day)<10:
       day_parse="0"+day
    else:
       day_parse=day
    year_parse=user_string[2]
    comps=[]
    comps.append(month_parse)
    comps.append(day_parse)
    comps.append(year_parse)
    parsed_date="/".join(comps)
    return parsed_date
#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
   list1=[]
   counter=0
   u_input1=input()
   '''while counter>0:
    if u_input1==-1:
       counter+=1
    else:'''
   list1=u_input1.split()
   print(parse_date(list1))

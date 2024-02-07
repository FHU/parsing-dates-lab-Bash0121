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
    list1=[]
    list1=user_string.split()

    month_parse=parse_month(list1[0])
    day=list1[1]
    day=day.replace(",","")

    if int(day)<10:
       day_parse="0"+day
    else:
       day_parse=day

    year_parse=list1[2]
    comps=[]
    comps.append(month_parse)
    comps.append(day_parse)
    comps.append(year_parse)
    parsed_date="/".join(comps)
    return parsed_date
#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
   u_input1=input()
   print(parse_date(u_input1))

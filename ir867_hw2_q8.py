# Indra 
# CS - UY 1114
# 24 Sept 2018
# Homework 2
days_a = int(input("Please enter the number of days Alice has worked: "))
hours_a = int(input("Please enter the number of hours Alice has worked: "))
minutes_a = int(input("Please enter the number of minutes Alice has worked: "))
days_b = int(input("Please enter the number of days Bob has worked: "))
hours_b = int(input("Please enter the number of hours Bob has worked: "))
minutes_b = int(input("Please enter the number of minutes Bob has worked: "))


days_t = (days_a+days_b)*1440
hours_t = (hours_a+hours_b)*60
minutes_t= minutes_a+minutes_b
total = days_t+hours_t+minutes_t

days_total = total//1440
hours_total = (total%1440)//60
minutes_total = (total%1440)%60
print("The total time both of them worked together is: "+str(days_total)+" days, "+str(hours_total)+" hours and "+str(minutes_total)+" minutes.")
                

import time
timestamp=int(time.strftime('%H'))
print("\n\n\n")
print("-"*50)
while 1:
    if(timestamp>=5 and timestamp<12):
        h=time.strftime("%H")
        m=time.strftime("%M")
        s=time.strftime("%S")
        print("Good Morning ShubhamSir\t\t Current Time:\t", h,"(Hours)", m, "(Minutes)", s, "(Seconds)")
        
    elif(timestamp>=12 and timestamp<16.30):
        h=time.strftime("%H")
        m=time.strftime("%M")
        s=time.strftime("%S")
        print("Good Afternoon ShubhamSir\t\t Current Time:\t", h,"(Hours)", m, "(Minutes)", s, "(Seconds)")
        

    elif(timestamp>16.31 and timestamp<18.30):
        h=time.strftime("%H")
        m=time.strftime("%M")
        s=time.strftime("%S")
        print("Good evening Shubham Sir. I hope your day was good.\t\t Current Time:\t", h,"(Hours)", m, "(Minutes)", s, "(Seconds)")
        
    elif(timestamp>=18.31):
        h=time.strftime("%H")
        m=time.strftime("%M")
        s=time.strftime("%S")
        print("Good Night ShubhamSir. Sweet Dreams\t\t Current Time:\t", h,"(Hours)", m, "(Minutes)", s, "(Seconds)")

    else:
        print("There is some mistake in my program. Please do check the program...!")
timestamp=time.strftime('%H')
print(timestamp,"(Hours)", end=", ")
timestamp=time.strftime('%M')
print(timestamp ,"(Minutes)", end=", ")
timestamp=time.strftime('%S')
print(timestamp,"(Seconds)")

print("-"*50)
print("\n\n")

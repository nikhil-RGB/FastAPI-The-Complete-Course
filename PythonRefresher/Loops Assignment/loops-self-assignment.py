my_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
i=0;
while i<3:
    for day in my_list:
        if(day=="Monday"):
            continue
        print(day+" ")
    print("\n") 
    i+=1;   

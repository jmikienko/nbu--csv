

# open netbackup config file - output of bppllist -L -allpolicies
streamPolicies = open("bppllist.txt")

# for each policy generate line
while 1 == 1:
    policy = streamPolicies.readline()
    tab_params = policy.split(" ")

    if tab_params[0] == "END":
        print("END")
        break

    if tab_params[0] == "CLASS":
        print ("POLICY: ", tab_params)

    if tab_params[0] == "INFO":
        print ("INFO: ", tab_params)

    if tab_params[0] == "SCHED":
        print ("SCHED: ", tab_params)
        if tab_params[2] == "0":
            print("this is full schedule")
        print("it runs every", tab_params[4], "seconds")
        print("its retention level is", tab_params[5])

    if tab_params[0] == "SCHEDWIN":
        print ("WINDOW: ", tab_params)
        for i in [1,3,5,7,9,11,13]:
            st_hour=int (tab_params[i])
            st_hour /=  3600
            st_minute = int (tab_params[i+1])
            print ("it starts at ", st_hour)
            print("and finishes an", st_minute/3600, "hours later")




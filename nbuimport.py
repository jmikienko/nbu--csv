

# open netbackup config file - output of bppllist -L -allpolicies
streamPolicies = open("C:\\Users\\jmikienko\\Desktop\\bppllist.txt")

# for each policy generate line
while 1 == 1:
    policy = streamPolicies.readline()
    tab_params = policy.split(" ")

    if tab_params[0] == "END":
        print("END")
        break

    if tab_params[0] == "CLASS":
        print ("POLICY," + tab_params[1])

    if tab_params[0] == "SCHED":
        print ("SCHED," + tab_params[1])
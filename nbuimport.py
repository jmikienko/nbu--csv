

# open netbackup config file - output of bppllist -L -allpolicies
streamPolicies = open("bppllist.txt")

nbu_retention_levels = {
    "0" : "1 week",
    "1": "2 weeks",
    "2": "3 weeks",
    "3" : "1 month",
    "4": "2 months",
    "5": "3 months",
    "6": "6 months",
    "7": "9 months",
    "8" : "1 year",
    "9": "infinite",
     }

nbu_policy_type = {
"0" : "Standard (UNIX and Linux clients)",
"1" : "Proxy",
"4" : "Oracle",
"6" : "Informix-On-BAR",
"7" : "Sybase",
"8" : "MS-SharePoint portal server",
"11" : "DataTools-SQL-BackTrack",
"13" : "MS- Windows",
"15" : "MS-SQL-Server",
"16" : "MS-Exchange-Server",
"17" : "SAP",
"18" : "DB2",
"19" : "NDMP",
"20" : "FlashBackup",
"21" : "Splitmirror",
"25" : "Lotus Notes",
"29" : "FlashBackup-Windows",
"35" : "NBU-Catalog",
"36" : "Generic",
"38" : "PureDisk export",
"39" : "Enterprise_Vault",
"40" : "VMware",
"41" : "Hyper-V",
"44" : "BigData"
}


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
        print ("INFO: This policy is ", nbu_policy_type[tab_params[1]], "policy")

    if tab_params[0] == "SCHED":
        print ("SCHED: ", tab_params)
        if tab_params[2] == "0":
            print("this is full schedule")
        if tab_params[2] == "1":
            print("this is differential schedule")
        if tab_params[2] == "2":
            print("this is cumulative incrmental schedule")

        print("it runs every", int(tab_params[4])/3600, "hours")
        print("its retention level is", tab_params[5])
        print("it keeps data for", nbu_retention_levels[tab_params[5]])

    if tab_params[0] == "SCHEDWIN":
        print ("WINDOW: ", tab_params)
        for i in [1,3,5,7,9,11,13]:
            st_hour=int (tab_params[i])
            st_hour /=  3600
            st_minute = int (tab_params[i+1])
            print ("it starts at ", st_hour)
            print("and finishes an", st_minute/3600, "hours later")






# open netbackup config file - output of bppllist -L -allpolicies
streamPolicies = open("bppllist.txt")

# constants definitions

# dictionary of NetBackup retention levels
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


nbu_ret_level_days = {
    "0" : "7",
    "1": "14",
    "2": "21",
    "3" : "31",
    "4": "62",
    "5": "93",
    "6": "186",
    "7": "279",
    "8" : "365",
    "9": "1000",
     }
# dictionary of NetBackup policy types

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

nbuDayOfWeek = {
    1 : "KSUNDAY",
    3 : "KMONDAY",
    5 : "KTUESDAY",
    7 : "KWEDNESDAY",
    9 : "KTHURSDAY",
    11 : "KFRIDAY",
    13 : "KSATURDAY"
}


# Variable definitions
# vPolicyName - saved NBU policy name
# vPolicyType - saved NBU policy type
# vScheduleType - saved NBU schedule type
# vRpoInterval

vPolicyType = ""
# for each policy generate line

numberOfLinesRead = 0

while 1 == 1:
    policy = streamPolicies.readline()
    numberOfLinesRead += 1
    tab_params = policy.split(" ")

    if tab_params[0] == "END":
        print("END")
        break

    if tab_params[0] == "CLASS":
        # print RPO of a previous Policy
        if numberOfLinesRead > 1:
            print("RPO,", vPolicyType)
        vPolicyName = tab_params[1]
  #      print ("POLICY: ", vPolicyName)

    if tab_params[0] == "INFO":
        vPolicyType = nbu_policy_type[tab_params[1]]
   #     print ("RPO," , vPolicyType)

    if tab_params[0] == "SCHED":
  #      print ("SCHED: ", tab_params)
        if tab_params[2] == "0":
            vSchedType = "Full"
  #          print("this is ", vSchedType)
        if tab_params[2] == "1":
            vSchedType = "Incr"
   #         print("this is", vSchedType )
        if tab_params[2] == "2":
            vSchedType = "Incr"
#          print("this is ", vSchedType)
        vRpoInterval = int(tab_params[4])/3600
 #       print("it runs every", vRpoInterval , "hours")

        vRet_days = nbu_ret_level_days[tab_params[5]]

        print("POLICY," , vPolicyName.strip() ,",some description," , vRet_days , "," , vRet_days , "," , vRet_days)

    if tab_params[0] == "SCHEDWIN":
 #       print ("WINDOW: ", tab_params)
        print("SCHED,", vSchedType, ",some desc,rpo,,,,,KHOURS," , int(vRpoInterval) , ",,,,,,,,,,")
        for i in [1,3,5,7,9,11,13]:
            vBkoutEnd = 0
            vStartHour=int (tab_params[i])
            vStartHour /=  3600
            vDuration = int (tab_params[i+1])
 #          print ("it starts at ", vStartHour)
 #          print("and finishes an", vDuration/3600, "hours later")
            vBkoutStart = (vStartHour+vDuration/3600)
            if vBkoutStart>24: vBkoutStart -= 24
            vBkoutDayOfWeek = nbuDayOfWeek[i]
            print("BKO_PERIOD," , vBkoutDayOfWeek , "," , int(vBkoutEnd) , ", 0 ," , int(vBkoutStart), ", 0")




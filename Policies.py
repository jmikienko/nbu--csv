#import uuid
#from sys_classes import Policy, CohesityAuth

# auth - class Cohesity Auth
# input - class Policy

def policy_generate(auth, policy):
    filename = "files/" + "cohesity_import_" + uuid.uuid4().hex + ".py"
    f = open(filename, "w+")

    f.write("from cohesity_management_sdk.cohesity_client import CohesityClient\n")

    f.write("username = '" + auth.username + "'\n")
    f.write("password = '" + auth.password + "'\n")
    f.write("domain = '" + auth.domain + "'\n")
    f.write("cluster_vip = 'prod-cluster.eng.cohesity.com'\n")

    f.write("client = CohesityClient(cluster_vip, username, password, domain)\n")

    f.write("client.config.skip_ssl_verification = True\n")

    f.write("protection_policies_controller = client.protection_policies\n")

    f.write("body = ProtectionPolicyRequest()\n")
    f.write("body.days_to_keep = " + str(policy.daysToKeep) + "\n")
    f.write("body.days_to_keep_log = " + str(policy.daysToKeepLog) + "\n")
    f.write("body.days_to_keep_system = " + str(policy.daysToKeepSystem) + "\n")
    f.write("body.description = '" + policy.description + "'\n")

    f.write("result = protection_policies_controller.create_protection_policy(body)\n")

    f.close()

    return filename

class Schedule:
    type = ""
    description = ""
    frequencyType = ""
    dayForWeekly = ""
    dayForMonthly = ""
    weekForMonthly = ""
    intervalMinutes =""
    intervalUnitForRPO = ""
    multiplyerOfInterval = ""

    def __init__(self):
        self.type = ""



def schedule_generate(schedule):
    if schedule.type == "full":
        pythCode = "body.full_scheduling_policy = SchedulingPolicy()"



    return pythCode

term=Schedule()
term.type = "full"
print (schedule_generate(term))
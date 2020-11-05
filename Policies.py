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
        pythCode = """body.full_scheduling_policy = SchedulingPolicy()
body.full_scheduling_policy.continuous_schedule = ContinuousSchedule()
body.full_scheduling_policy.daily_schedule = DailySchedule()
body.full_scheduling_policy.rpo_schedule = RpoSchedule() """


    if schedule.type == "incr":
        pythCode = """body.incremental_scheduling_policy = SchedulingPolicy()
body.incremental_scheduling_policy.continuous_schedule = ContinuousSchedule()
body.incremental_scheduling_policy.daily_schedule = DailySchedule()
body.incremental_scheduling_policy.monthly_schedule = MonthlySchedule()
body.incremental_scheduling_policy.rpo_schedule = RpoSchedule()"""

    if schedule.type == "log":
        pythCode = """body.log_scheduling_policy = SchedulingPolicy()
body.log_scheduling_policy.continuous_schedule = ContinuousSchedule()
body.log_scheduling_policy.daily_schedule = DailySchedule()
body.log_scheduling_policy.monthly_schedule = MonthlySchedule()
body.log_scheduling_policy.rpo_schedule = RpoSchedule()
"""

    return pythCode

def rpo_generate(rpo):

    pythCode = """ body.rpo_policy_settings = RpoPolicySettings()
body.rpo_policy_settings.alerting_config = AlertingConfig()
body.rpo_policy_settings.environment_type_job_params = EnvironmentTypeJobParameters()
body.rpo_policy_settings.environment_type_job_params.aws_snapshot_parameters = AwsSnapshotManagerParameters()
body.rpo_policy_settings.environment_type_job_params.hyperv_parameters = HypervEnvJobParameters()
body.rpo_policy_settings.environment_type_job_params.nas_parameters = NasEnvJobParameters()
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters = DataMigrationJobParameters()
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters.cold_file_window = 2
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters.file_path_filter = FilePathFilter()
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters.file_path_filter.exclude_filters = ['23']
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters.file_path_filter.protect_filters = ['23']
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters.file_selection_policy = FileSelectionPolicyEnum.KOLDERTHAN
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters.file_size_bytes = 32
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters.file_size_policy = FileSizePolicyEnum.KGREATERTHAN
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters.nfs_mount_path = 'dfsd'
body.rpo_policy_settings.environment_type_job_params.nas_parameters.data_migration_job_parameters.target_view_name = 'dfsf'
body.rpo_policy_settings.environment_type_job_params.nas_parameters.enable_faster_incremental_backups = True
body.rpo_policy_settings.environment_type_job_params.nas_parameters.file_path_filters = FilePathFilter()
body.rpo_policy_settings.environment_type_job_params.nas_parameters.file_path_filters.exclude_filters = ['wfe']
body.rpo_policy_settings.environment_type_job_params.nas_parameters.file_path_filters.protect_filters = ['edwe']
body.rpo_policy_settings.environment_type_job_params.nas_parameters.nas_protocol = NasProtocolNasEnvJobParametersEnum.KNFS3
body.rpo_policy_settings.environment_type_job_params.office_365_parameters = Office365EnvJobParameters()
body.rpo_policy_settings.environment_type_job_params.office_365_parameters.onedrive_parameters = OneDriveEnvJobParameters()
body.rpo_policy_settings.environment_type_job_params.office_365_parameters.onedrive_parameters.file_path_filter = FilePathFilter()
body.rpo_policy_settings.environment_type_job_params.office_365_parameters.outlook_parameters = OutlookEnvJobParameters()
body.rpo_policy_settings.environment_type_job_params.office_365_parameters.outlook_parameters.file_path_filter = FilePathFilter()
body.rpo_policy_settings.environment_type_job_params.physical_parameters = PhysicalEnvJobParameters()
body.rpo_policy_settings.environment_type_job_params.physical_parameters.file_path_filters = FilePathFilter()
body.rpo_policy_settings.environment_type_job_params.pure_parameters = SanEnvJobParameters()
body.rpo_policy_settings.environment_type_job_params.sql_parameters = SqlEnvJobParameters()
body.rpo_policy_settings.environment_type_job_params.vmware_parameters = VmwareEnvJobParameters()
body.rpo_policy_settings.indexing_policy = IndexingPolicy()

    """
    return pythCode

def bko_period_generate(bko_period):
    pythcode = """ body.blackout_periods = []
body.blackout_periods.append(BlackoutPeriod())
body.blackout_periods[0].end_time = TimeOfDay()
body.blackout_periods[0].end_time.hour = 2
body.blackout_periods[0].end_time.minute = 2
body.blackout_periods[0].start_time = TimeOfDay()
body.blackout_periods[0].start_time.hour = 3
body.blackout_periods[0].start_time.minute = 3
    """
    return pythcode

def

term=Schedule()
term.type = "incr"
print (schedule_generate(term))
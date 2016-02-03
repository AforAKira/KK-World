#! /usr/bin/python
# :beginHead

# :author               :kiran-an
# :support              :kiran-an
# :type                 :Python
# :title                :Job spread
# :description          :Job spread script for Advertising

# :endHead
# import os

import subprocess

jCode = 0
joN = input(" \n 1. Job Name \n 2. Job Code \n\n Select an option from above :")
if joN == '1':
    jobName = input("\n Enter proper Job Name :")
    if '_' in jobName:
        aSplit = jobName.split('_')
        jCode = aSplit[1]
    else:
        print("\nScript Info: Enter valid Job name..")
elif joN == '2':
    jCode = input("\nEnter Job code/Id:")
else:
    print ("\nScript Info:Please enter valid Option::")
if jCode != 0:
    jobList = subprocess.getoutput('ls /jobs/')
    if jCode in jobList:
        print("\n Script Info: Job exists in Bangalore\n")
    else:
        jobId = jCode[0:2]
        if jobId == '14':
            print ("\nScript Info: Searching job in London..")
            jobOutput = subprocess.Popen(["ssh", "lnda-vnc.mpc.local","ls ", "/jobs", "|", "grep", jCode],stdout=subprocess.PIPE)
            jName = jobOutput.communicate()[0]
            jStatus = jobOutput.returncode
            if (jStatus == 1):
                print("\nScript Info: Job not existed in London..")
            elif (jStatus == 0):
                print("\nScript Info: Job existed in London..")
                print("\nScript Info: Spreading Job to London for you..")
                jobspreadOutput = subprocess.call(["jobinator", "-j", jName, "-p", "tvc-combined", "-s", "bang,agni1"])
                print("\nScript Info: Job spread Output", jobspreadOutput)
        elif jobId == '54':
            print ("\nScript Info: Searching job in NYCB")
            jobOutput = subprocess.Popen(["ssh", "nycb-vnc.nycb.mpc.local","ls ", "/jobs", "|", "grep", "jCode"],
                                         stdout=subprocess.PIPE)
            jName = jobOutput.communicate()[0]
            jStatus = jobOutput.returncode
            if (jStatus == 1 ):
                print("\nScript Info: Job not existed in NYCB..!")
            elif (jStatus == 0):
                print("\nScript Info: Job existed in NYCB..")
                print("\nScript Info: Spreading Job to NYCB..")
                jobspreadOutput = subprocess.call(["jobinator", "-j", jName, "-p", "tvc-combined", "-s", "bang,agni1"])
                print("\nScript Info: Job spread Output", jobspreadOutput)
        elif jobId == '24':
            print ("\nScript Info: Searching job in STMN")
            jobOutput = subprocess.Popen(["ssh", "stmn-vnc.stmn.mpc.local","ls ", "/jobs", "|", "grep", "jCode"],stdout=subprocess.PIPE)
            jName = jobOutput.communicate()[0]
            jStatus = jobOutput.returncode
            if (jStatus == 1):
                print("\nScript Info: Job not existed in STMN..")
            elif (jStatus == 0):
                print("\nScript Info: Job existed in STMN..")
                print("\nScript Info: Spreading Job to STMN..")
                jobspreadOutput = subprocess.call(["jobinator", "-j", jName, "-p", "tvc-combined", "-s", "bang,agni1"])
                print("\nScript Info: Job spread Output", jobspreadOutput)
        elif jobId == "61":
            print ("\nScript Info: Searching job in Amsterdam")
            jobOutput = subprocess.Popen(["ssh", "lnda-vnc.mpc.local","ls ", "/jobs", "|", "grep", "jCode"],stdout=subprocess.PIPE)
            jName = jobOutput.communicate()[0]
            jStatus = jobOutput.returncode
            if (jStatus == 1):
                print("\nScript Info: Job not existed in Amsterdam..")
            elif (jStatus == 0):
                print("\nScript Info: Job existed in Amsterdam..")
                print("\nScript Info: Spreading Job to Amsterdam..")
                jobspreadOutput = subprocess.call(["jobinator", "-j", jName, "-p", "tvc-combined", "-s", "bang,agni1"])
                print("\nScript Info: Job spread Output", jobspreadOutput)
        elif jobId == "64":
            print ("\nScript Info: Searching job in Mexico")
            jobOutput = subprocess.Popen(["ssh", "mext-vnc.mext.mpc.local","ls ", "/jobs", "|", "grep", "jCode"],stdout=subprocess.PIPE)
            jName = jobOutput.communicate()[0]
            jStatus = jobOutput.returncode
            if (jStatus == 1):
                print("\nScript Info: Job not existed in Mexico..")
            elif (jStatus == 0):
                print("\nScript Info: Job existed in Mexico..")
                print("Spreading Job to Mexico .......")
                jobspreadOutput = subprocess.call(["jobinator", "-j", jName, "-p", "tvc-combined", "-s", "bang,agni1"])
                print("\nScript Info: Job spread Output", jobspreadOutput)
        elif jobId == "74":
            print ("\nScript Info: Searching job in Paris")
            jobOutput = subprocess.Popen(["ssh", "lnda-vnc.mpc.local","ls ", "/jobs", "|", "grep", "jCode"],stdout=subprocess.PIPE)
            jName = jobOutput.communicate()[0]
            jStatus = jobOutput.returncode
            if (jStatus == 1):
                print("\nScript Info: Job not existed in Paris..")
            elif (jStatus == 0):
                print("Job existed in Paris ::")
                print("Spreading Job to Paris .......")
                jobspreadOutput = subprocess.call(
                    ["jobinator", "-j", jName, "-p", "tvc-combined", "-s", "bang,agni1"])
                print("\nScript Info: Job spread Output", jobspreadOutput)
        elif jobId == "84":
            print ("\nScript Info: Cant Spread job to Shanghai.. It has to be created in Bangalore it self\n")
        else:
            print("\nScript Info: Enter valid Job Id or Job name name\n")


#nycb-vnc.nycb.mpc.local
#stmn-vnc.stmn.mpc.local
#hendrix for Amterdam
#mext-vnc.mext.mpc.local

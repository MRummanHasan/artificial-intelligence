from pprint import pprint

####################################################################################
######################      ###############          ###############################
#####################  ####  ##################  ###################################
####################  ######  #################  ###################################
###################  ###  ###  ################  ###################################
##################  ##########  ###########          ###############################
####################################################################################

class Patient():
    def __init__(self, id):
        self.id = id
        self.RecomDis = {} # { } dist
        self.PresDis = "noPresDis"
        self.medicine = "nomedicine"
        self.medtime = "nomedtime"

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False


pat_IDs = 00
All_patient_ID = [] #remove after use
patArray = []
progFlow = -1
while(progFlow != 0):
    print("1-Patient\n2-Doctor\n3-Nurse\n4-Statistics\n0-Quit")
    typ = input("User type>>> ")
    if typ == '1':
        pat_IDs = pat_IDs + 1
        patArray.append(Patient(pat_IDs))
        All_patient_ID.append(pat_IDs)  #remove after use
        print("\nWELCOME Patient. Your ID is "+ str(pat_IDs) )
        print(All_patient_ID)  #remove after use

        # prediction work/ symptoms



    elif typ == '2':
        print("\nWELCOME DOCTOR ")
        doc = True
        while (doc):
            myPatID = input("Press 0-Quit\nEnter patient ID: ")            
            try:
                myPatID = int(myPatID)
                print(All_patient_ID)
                if contains(patArray, lambda x: x.id == myPatID):
                    for pat in patArray:
                        if pat.id == myPatID:
                            pprint(vars(pat)) # print(pat.id, pat.RecomDis, pat.PresDis, pat.medicine)
                            docInputType = input("1-Enter Prescribed Disease\n2-Change Patient\n0-Quit\n> ")
                            if docInputType == '1':
                                pat.PresDis = input("Enter Disease u found: ")
                            elif docInputType == '2':
                                break
                            elif docInputType == '0':
                                doc = False
                elif myPatID == '0':
                    doc = False
                else:
                    print("Patient ID not found !!!")
            
            except:
                print("ERROR : invalid ID")
                break
            

        
    elif typ == '3':
        print("\nWELCOME NURSE ")
        doc = True
        while (doc):
            myPatID = input("Enter patient ID: ")
            try:
                myPatID = int(myPatID)
                print(All_patient_ID)
                if contains(patArray, lambda x: x.id == myPatID):
                    for pat in patArray:
                        if pat.id == myPatID:
                            print("Your Patient's Data")
                            pprint(vars(pat)) # print(pat.id, pat.RecomDis, pat.PresDis, pat.medicine)
                            docInputType = input("1-Enter Prescribed Disease\n2-Change Patient\n0-Quit\n> ")
                            if docInputType == '1':
                                pat.medicine = input("Medicine you suggested: ")
                                pat.medtime = input("Medicine Time: ")
                            elif docInputType == '2':
                                break
                            elif docInputType == '0':
                                doc = False
                elif myPatID == '0':
                    doc = False
                else:
                    print("Patient ID not found !!!")
            
            except:
                print("ERROR : invalid ID")
                break

        
        
    elif typ == '4':
        print("WELCOME! researcher")
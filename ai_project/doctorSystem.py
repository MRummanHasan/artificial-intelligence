from pprint import pprint

####################################################################################
######################      ###############          ###############################
#####################  ####  ##################  ###################################
####################  ######  #################  ###################################
###################  ##    ##  ################  ###################################
##################  ##########  ###########          ###############################
####################################################################################

class Patient():
    def __init__(self, id):
        self.id = id
        self.RecomDis = {} # { } dist
        self.PresDis = "noPresDis"
        self.medicine = "nomedicine"
        self.medtime = "nomedtime"

class Doctor():
    def __init__(self, name, dept, timeTo, timeFrom, location, price):
        self.name = name
        self.dept = dept
        self.timeTo = timeTo
        self.timeFrom = timeFrom
        self.location = location
        self.price = price
class Disease():
    def __init__(self, name, mainSymp, nSymp):
        self.name = name
        self.mainSymp = mainSymp
        self.nSymp = nSymp
        self.nAns = []


with open("diseaseData.txt", "r") as ins:
    DiseaseArray = []
    for line in ins:
        line = line.strip().split(',')
        a = line[3].strip().split(' ')
        print(a)
        DiseaseArray.append(line)

print(DiseaseArray)

listofAllsymp={
    "Deep Cough":["ear-Pain", "sore-Swelling", "change-in-Voice", "difficulty-in-breathing"],
    "MainSymp3": ["weakness", "Fever", "cheek-swelling", "other", "other2"],
    "Nose Bleeding": ['Noisy-Breathing','Bad-Breath', 'Loose-Weight'],
    'lung problems':['cough-with-blood', 'shortness-of-breath'],
    "Red-Patch-in-the-Mouth":['Weakness-in-Body','Fatigue'],
    'skin problems':['redness-of-face','moles-on-skin'],
    'Diarrhea': ['watery-stool', 'vomiting','abdominal-cramps','belly-pain'],
    'Eating or Weight Problems': ['W', 'Fever']
}
def populateDisease():
    tempdataArray = []
    i = 0
    # print("Disease - MainSymptom - [Specific Symptoms]")
    for k, v in listofAllsymp.items():
        tempdataArray.append(Disease("Disease"+str(i), k, v))
        # print(disArray[i].name, disArray[i].mainSymp, disArray[i].nSymp)
        i = i + 1
    return tempdataArray

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

##################################################################################################
disArray = []
tempdataArray = populateDisease()
indexofdis = []
userSymp = []
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
        for d in tempdataArray:
            ans = input("Answer with 'y' or 'n'\nDo you have/feel " + str(d.mainSymp) + " >>> ")
            indexofdis = indexofdis + 1
            if ans == "y":
                disArray.append(d)
                for n in d.nSymp:
                    if n not in userSymp:

                        NSans = input("\nDo you have/feel "+str(n)+" : \n4-Very much, 3-Yes, 2-Slightly, 1-Not at all : ")
                        if NSans == '1':
                            d.nAns.append(0)
                        elif NSans == '2':
                            d.nAns.append(0.4)
                        elif NSans == '3':
                            d.nAns.append(0.8)
                        elif NSans == '4':
                            d.nAns.append(1)
                            tempdataArray = tempdataArray[0:indexofdis]

                            userSymp.append(n) #users most symptom
                            print("usre symp", userSymp)

                            with open("diseaseData.txt", "r") as ins:
                                for line in ins:
                                    if all(elem in line for elem in userSymp):
                                        line = line.strip().split(',')
                                        a = line[3].strip().split(' ')
                                        tempdataArray.append(Disease(line[1],line[2],a))         




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
                            print(pat.id, pat.RecomDis, pat.PresDis, pat.medicine)
                            docInputType = input("1-Enter Prescribed Disease\n2-Change Patient\n0-Quit\n> ")
                            if docInputType == '1':
                                pat.PresDis = input("Enter Disease u found: ")
                                # pprint(vars(pat))
                            elif docInputType == '2':
                                break
                            elif docInputType == '0':
                                doc = False
                elif myPatID == 0:
                    doc = False
                    print("i said break")
                else:
                    print("Patient ID not found !!!")
            
            except:
                print("ERROR : invalid ID")                    
                break
        
    elif typ == '3':
        print("\nWELCOME NURSE ")
        nurse = True
        while (nurse):
            myPatID = input("Enter patient ID: ")
            try:
                myPatID = int(myPatID)
                print(All_patient_ID)
                if contains(patArray, lambda x: x.id == myPatID):
                    for pat in patArray:
                        if pat.id == myPatID:
                            print("Your Patient's Data: ",pat.id, pat.RecomDis, pat.PresDis, pat.medicine)
                            print()
                            docInputType = input("1-Enter Prescribed Disease\n2-Change Patient\n0-Quit\n> ")
                            if docInputType == '1':
                                # confirmation work
                                pat.medicine = input("Medicine you suggested: ")
                                pat.medtime = input("Medicine Time: ")
                                pprint(vars(pat))
                            elif docInputType == '2':
                                break
                            elif docInputType == '0':
                                nurse = False
                elif myPatID == 0:
                    nurse = False
                else:
                    print("Patient ID not found !!!")
            
            except:
                print("ERROR : invalid ID")
                break

        
        
    elif typ == '4':
        print("WELCOME! researcher")
        for diseaseDetails in tempdataArray:
            print(diseaseDetails.name, diseaseDetails.mainSymp,
                diseaseDetails.nSymp, diseaseDetails.nAns)


# from pprint import pprint
import pymysql
# from scipy.spatial import distance
# import numpy

print("\n<<< Welcome to the IntelliHealth >>>\n")

print("##########################################################################")
print("######################      ###############          #####################")
print("#####################  ####  ##################  #########################")
print("####################  ######  #################  #########################")
print("###################  ##    ##  ################  #########################")
print("##################  ##########  ###########          #####################")
print("##########################################################################")

# # SQL connection work
conn = pymysql.connect(host='localhost', user='root',
                       password='', db='HealthSystem')
sq = conn.cursor()
# # end connection work


class Patient():
    def __init__(self, id):
        self.id = id
        self.RecomDis = []  # { } dist
        self.PresDis = "no-Prescribed-Disease"
        self.medicine = "no-Medicine-Suggested"
        self.medtime = "no medtime"
        self.hosp = "no-Hosp-Assigned"


user_location = [3, 5]


class Doctor():
    def __init__(self, name, dept, timeTo, timeFrom, location, price):
        self.name = name
        self.dept = dept
        self.timeTo = timeTo
        self.timeFrom = timeFrom
        self.location = location
        self.price = price


class Disease():
    def __init__(self, name, mainSymp, nSymp, crVal):
        self.name = name
        self.mainSymp = mainSymp
        self.nSymp = nSymp
        self.crVal = crVal
        self.nAns = []


initialDisease = {
    # disease_ID, disease_Name, Main_Symptom, [Specific_Symptoms1, Specific_Symptoms2, Specific_Symptoms...], [Crtitical Value against Specific_Symptoms]
    "1, Laryngeal Cancer,  Deep Cough, ear-Pain sore-Swelling change-in-Voice difficulty-in-breathing, 0.8 0.4 0.2 0.1",
    "2, Convulsion Cancer,swollen eye, weakness Fever cheek-swelling, 0.8 0.4 0.2 0.1",
    "3, Leather Allergy, skin problems, redness-of-face moles-on-skin, 0.8 0.4 0.2 0.1",
    "4, Diarrhea, watery-stool, vomiting abdominal-cramps belly-pain, 0.8 0.4 0.1",
    "5, Obesity, Weight Problems, vomiting Fever, 0.8 0.1"}
tempdataArray = []
# print(initialDisease)
for eachdoc in initialDisease:
    eachdoc = eachdoc.strip().split(',')
    a = eachdoc[3].strip().split(' ')
    criticValue = eachdoc[4].strip().split(' ')
    tempdataArray.append(Disease(eachdoc[1], eachdoc[2], a, criticValue))


# distance cost of hospitals
dist_of_Hosp = {
    'Nazimabad Hospital': [5, 2],
    'Johar Hospital': [1, 1],
    'DHA Hospital': [3, 8],
    'Saddar Skin Hospital': [5, 5]
}


def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

# # INPUR: Nothing
# # OUTPUT: raw data of doctor
# # FUNC: fetch data from SQL


def fetchDatafromSQL(thisdepart):
    sql = 'SELECT doc_name,doc_dept,doc_TimeTo, doc_timeFrom,doc_location,doc_price FROM doctor WHERE doc_dept = '+'"'+thisdepart+'"'
    a.execute(sql)
    data = a.fetchall()
    # print(data)
    return data

# # INPUR: Calculated-percentages of symptoms by User, Disease-to-Depart Data
# # OUTPUT: Specific department name as patients symptoms
# # FUNC: Check Department


def check_depart(symp_percent, Disease_to_dept):
    highVal = 0
    inverse = [(value, key) for key, value in symp_percent.items()]
    try:
        highVal = max(inverse)[0]
    except:
        pass

    # Key at highest value
    if highVal != 0.0:
        highValKey = list(symp_percent.keys())[
            list(symp_percent.values()).index(highVal)]
    else:
        return 'General'

    for dtdk, dtdv in Disease_to_dept.items():
        if dtdv.__contains__(highValKey):
            # print("success this depart: ")
            return dtdk  # matched deaprtment

    return 'General'


Disease_to_dept = {
    'ENT': ['Disease0', 'Disease1'],
    'General': ['Influenza', 'Obesity'],
    'Cancer': ['Oral', 'Laryngeal Cancer'],
    'Skin': ['Leather Allergy', 'Disease6'],
    'Dentist': ['ToothAche', 'Disease8'],
    'OPD': ['D0', 'Diarrhea'],
    'Psychology': ['Disease2', 'Disease4']
}

##################################################################################################
# # STEP: 1
# populate/fetch data
# tempdataArray = []
disArray = []
with open("diseaseData.txt", "r") as ins:
    for line in ins:
        line = line.strip()
        line = line.strip().split(',')
        a = line[3].strip().split(' ')
        criticValue = line[4].strip().split(' ')
        tempdataArray.append(Disease(line[1], line[2], a, criticValue))

# for diseaseDetails in tempdataArray:
#     pprint(vars(diseaseDetails))
# # STEP: 2
# main working
indexofdis = 0
pat_IDs = 00
All_patient_ID = []  # remove after use
patArray = []
progFlow = -1

while(progFlow != 0):
    print("1-Patient\n2-Doctor\n3-Nurse\n4-Statistics\n0-Quit")
    typ = input("User type>>> ")

    if typ == '1':
        userSymp = []
        pat_IDs = pat_IDs + 1
        patArray.append(Patient(pat_IDs))
        All_patient_ID.append(pat_IDs)  # remove after use

        print("\nWELCOME Patient. Your ID is " + str(pat_IDs))
        # print(All_patient_ID)  # remove after use

        # prediction work/ symptoms
        for d in tempdataArray:
            ans = input("Answer with 'y' or 'n'\nDo you have/feel " +
                        str(d.mainSymp) + " >>> ")
            indexofdis = indexofdis + 1
            if ans == "y":
                disArray.append(d)
                i = 0
                for n in d.nSymp:

                    if n not in userSymp:

                        NSans = input(
                            "\nDo you have/feel "+str(n)+" : \n4-Very much, 3-Yes, 2-Slightly, 1-Not at all : ")

                        if NSans > d.crVal[i]:

                            tempdataArray = tempdataArray[0:indexofdis]

                            userSymp.append(n)  # users most symptom
                            print("usre symp", userSymp)

                            with open("diseaseData.txt", "r") as ins:
                                for line in ins:
                                    if all(elem in line for elem in userSymp):
                                        line = line.strip().split(',')
                                        a = line[3].strip().split(' ')
                                        criticValue = line[4].strip().split(
                                            ' ')
                                        tempdataArray.append(
                                            Disease(line[1], line[2], a, criticValue))
                    i = i+1
        # # STEP: 3
        # # Calculate percentage of symptom occurance
        symp_percent = {}
        for dispercent in disArray:
            ansSize = sum(dispercent.nAns)
            tsymp = len(dispercent.nSymp)
            per = (ansSize / tsymp) * 100
            symp_percent[dispercent.name] = per

        possibleDisease = []
        for k, v in symp_percent.items():
            if v != 0.0:
                possibleDisease.append([k, str(v)+" %"])
        patArray[pat_IDs-1].RecomDis.append(possibleDisease)
        print(possibleDisease)

        '''           
        def findNearestHosp(dist_of_Hosp, disArray):
            for eachdoc in disArray:
                AllhospCordinates = []
                # # Contraints for Location
                hosp_cord = dist_of_Hosp[eachdoc.location]

                user_points = (user_location[0], user_location[1], 0)
                hosp_points = (hosp_cord[0], hosp_cord[1], 0)
                dst = numpy.linalg.norm( user_points-hosp_points)
                # scipy.spatial.distance.euclidian(minimal, maximal)
                # dst = distance.euclidean(user_points, hosp_points)
                # print(dst, "dsit from hosp")
                AllhospCordinates.append(dst)
            print()
            try:
                minVal = min(AllhospCordinates)
                indexof_hospCord = AllhospCordinates.index(minVal)
                print("Nearest Hospital is: ",
                    disArray[indexof_hospCord].location)
            except:
                print("Please visit your nearest Hospital")
        '''

        # # STEP: 4
        thisdepart = check_depart(symp_percent, Disease_to_dept)
        # print(thisdepart)

        # # STEP: 5
        # # Fetch data as per user entry

        # # INPUR: Nothing
        # # OUTPUT: raw data of doctor
        # # FUNC: fetch data from SQL
        sql = 'SELECT doc_name,doc_dept,doc_TimeTo, doc_timeFrom,doc_location,doc_price FROM doctor WHERE doc_dept = '+'"'+thisdepart+'"'
        sq.execute(sql)
        data = sq.fetchall()
        print(data)

        # # STEP: 7
        # # Tell nearest hospital
        # findNearestHosp(dist_of_Hosp, disArray)

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
                            print(pat.id, pat.RecomDis,
                                  pat.PresDis, pat.medicine)
                            docInputType = input(
                                "1-Enter Prescribed Disease\n2-Change Patient\n0-Quit\n> ")
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
            myPatID = input("0-Quit\nEnter patient ID: ")
            try:
                myPatID = int(myPatID)
                print(All_patient_ID)
                if contains(patArray, lambda x: x.id == myPatID):
                    for pat in patArray:
                        if pat.id == myPatID:
                            print("Your Patient's Data: ", pat.id,
                                  pat.RecomDis, pat.PresDis, pat.medicine)
                            print()
                            docInputType = input(
                                "1-Enter Medicine and Time\n2-Change Patient\n0-Quit\n> ")
                            if docInputType == '1':
                                # confirmation work
                                pat.medicine = input(
                                    "Medicine you suggested: ")
                                pat.medtime = input("Medicine Time: ")
                                print("Patient ID: ", pat.id, "\nDisease: ", pat.RecomDis,
                                      "\nMedicine: ", pat.medicine, "\nMedicine Timings: ", pat.medtime)
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
        # pandas csv work
        # import pandas as pd
        # data = pd.read_csv('diseaseData.txt')
        # print(data)
        docInputType = input(
            "1-Check disease detail\n2-check Patient detail\n0-Quit\n> ")
        if docInputType == '1':

            with open("diseaseData.txt", "r") as ins:
                for line in ins:
                    print(line)

        elif docInputType == '2':
            for pats in patArray:
                # pprint(vars(pats))
                print("Patient ID: ", pat.id, "\nPredicted Disease", pats.PresDis, "\nDisease: ",
                      pat.RecomDis, "\nMedicine: ", pat.medicine, "\nMedicine Timings: ", pat.medtime)

    elif typ == '0':
        print("Good Bye")
        break

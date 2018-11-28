import pymysql
from scipy.spatial import distance
import numpy
user_location = [2, 3]
user_price = 500
print("<<< Welcome to the IntelliHealth >>>\n")


class Disease():
    def __init__(self, name, mainSymp, nSymp):
        self.name = name
        self.mainSymp = mainSymp
        self.nSymp = nSymp
        self.nAns = []


class Doctor():
    def __init__(self, name, dept, timeTo, timeFrom, location, price):
        self.name = name
        self.dept = dept
        self.timeTo = timeTo
        self.timeFrom = timeFrom
        self.location = location
        self.price = price


# # SQL connection work
conn = pymysql.connect(host='localhost', user='root',
                       password='', db='HealthSystem')
a = conn.cursor()
# # end connection work
# # Query to fetch data from juntion/bridge table in SQL
# sql = 'SELECT Disease.disease_name, S.symptom_name FROM diseases AS Disease JOIN disease_symptoms_bridgetable AS DC ON Disease.disease_id = DC.disease_id JOIN symptoms AS S ON S.symptom_id = DC.symptom_id'
# a.execute(sql)
# # data = a.fetchall()
########################     OR   use this dummy data #####################
# # MainSymp : symp1, symp2....
listofAllsymp = {
    "Deep Cough": ["ear Pain", "sore Swelling", "change in Voice", "difficulty in breathing"],
    "Jaw Pain": ["sore Throat", "teeth Loose", "painful Chewing"],
    "MainSymp3": ["weakness", "Fever", "cheek swelling", "other", "other2"],
    "Nose Bleeding" :['Noisy Breathing' ,'Bad Breath', 'Loose Weight'],
    "Swelling in Cheeck":['Pain in Cheek','Pain Behind the nose','Loosing teeths for no reason'],
    'lung problems': ['cough with blood', 'shortness of breath'],
    "Red or Mouth Patch in the Mouth":['Weakness in Body','Fatigue'],
    'skin problems': ['redness of face', 'moles on skin'],
    'Diarrhea': ['watery stool', 'vomiting', 'abdominal cramps', 'belly pain'],
    'Eating or Weight Problems': ['W', 'Fever']
}


# # INPUT: Raw Data from SQL
# # OUTPUT: return Array of Objects of doctors-details
# # FUNC: Populate Doctor objects
def populateDoctor(data):
    doctorObjArray = []
    for eachdoc in data:
        doctorObjArray.append(
            Doctor(eachdoc[0], eachdoc[1], eachdoc[2], eachdoc[3], eachdoc[4], eachdoc[5]))
        ##       name,  dept,  timeTo,  timeFrom,  location,   price
        print("Dr.",eachdoc[0],"-", eachdoc[1],".Timings:", eachdoc[2],"-", eachdoc[3],"at", eachdoc[4],"Price:", eachdoc[5])

    return doctorObjArray


# # INPUT: Calculated-percentages of symptoms by User, Disease-to-Depart Data
# # OUTPUT: Specific department name as patients symptoms
# # FUNC: Check Department
def check_depart(symp_percent, Disease_to_dept):

    inverse = [(value, key) for key, value in symp_percent.items()]
    highVal = max(inverse)[0]

    ## Key at highest value
    if highVal != 0.0:
        highValKey = list(symp_percent.keys())[list(symp_percent.values()).index(highVal)]
    else:
        return 'General'

    for dtdk, dtdv in Disease_to_dept.items():
        if dtdv.__contains__(highValKey):
            # print("success this depart: ")
            return dtdk  # matched deaprtment

    return 'General'


# INPUT: nothing for now, BUT Raw Data from SQL
# # OUTPUT: return Array of Objects of disease-details
# # FUNC: Populate Disease from SQL-table to Disease-Objects
def populateDisease():
    disArray = []
    i = 0
    # print("Disease - MainSymptom - [Specific Symptoms]")
    for k, v in listofAllsymp.items():
        disArray.append(Disease("Disease"+str(i), k, v))
        # print(disArray[i].name, disArray[i].mainSymp, disArray[i].nSymp)
        i = i + 1
    return disArray

Disease_to_dept = {
    'ENT': ['Disease0', 'Disease1'],
    'General': ['Influenza', 'Disease3'],
    'Cancer': ['Oral', 'Disease4'],
    'Skin': ['Disease5', 'Disease6'],
    'Dentist': ['Disease7', 'Disease8'],
    'OPD': ['D0', 'Disease3'],
    'Psychology': ['Disease2', 'Disease4']
}

# distance cost of hospitals
dist_of_Hosp = {
    'Nazimabad Hospital': [5, 2],
    'Johar Hospital': [1, 1],
    'DHA Hospital': [3, 8],
    'Saddar Skin Hospital': [5, 5]
}

# # INPUR: Nothing
# # OUTPUT: raw data of doctor
# # FUNC: fetch data from SQL
def fetchDatafromSQL(thisdepart):
    sql = 'SELECT doc_name,doc_dept,doc_TimeTo, doc_timeFrom,doc_location,doc_price FROM doctor WHERE doc_dept = '+'"'+thisdepart+'"'
    a.execute(sql)
    data = a.fetchall()
    # print(data)
    return data



# # INPUR: obj-array of disease
# # OUTPUT: nothing
# # FUNC: print details of disease
def printDisease(diseaseObjArray):
    for diseaseDetails in diseaseObjArray:
        print(diseaseDetails.name, diseaseDetails.mainSymp,
              diseaseDetails.nSymp, diseaseDetails.nAns)
    print()


# # INPUR: distance cost of hospitals, Objedct array of doctors
# # OUTPUT: print Nearest Hospital Name
# # FUNC: search for nearest hospital to the patient
def findNearestHosp(dist_of_Hosp, doctorObjArray):
    for eachdoc in doctorObjArray:
        AllhospCordinates = []
        # # Contraints for Location
        hosp_cord = dist_of_Hosp[eachdoc.location]

        user_points = (user_location[0], user_location[1], 0)
        hosp_points = (hosp_cord[0], hosp_cord[1], 0)
        dst = distance.euclidean(user_points, hosp_points)

        AllhospCordinates.append(dst)
    print()
    try:
        minVal = min(AllhospCordinates)
        indexof_hospCord = AllhospCordinates.index(minVal)
        print("Nearest Hospital is: ",
              doctorObjArray[indexof_hospCord].location)
    except:
        print("Please visit your nearest Hospital")

disData =( (1, 'Disease1', 'Deep Cough', 'Ear Pain'),
       (1, 'Disease1', 'Deep Cough', 'Sore Swelling'),(1, 'Disease1', 'Deep Cough', 'Change in Voice'),(1, 'Disease1', 'Deep Cough', 'Difficulty in Breath'),(1, 'Disease1', 'Deep Cough','Difficulty in Breath'),(2, 'Disease2', 'Jaw Pain', 'Sore Throat'),(2, 'Disease2', 'Jaw Pain', 'Teeth Loose'),(2, 'Disease2', 'Jaw Pain', 'Painful Chewing'),(3, 'Disease3', 'MainSymp3', 'Weakness'),(3, 'Disease3', 'MainSymp3', 'Fever'),(3, 'Disease3', 'MainSymp3', 'Cheek Swelling') )
#################################################################################################################


# # STEP: 1
diseaseObjArray = populateDisease()
class Patient():
    def __init__(self, id):
        self.id = id
        self.RecomDis = {} # { } dist
        self.PresDis = "PresDis"
        self.medicine = "medicine"
        self.medtime = "medtime"

# # STEP: 2
# # ASK SYMPTOMS
pat_IDs = 0
All_patient_ID = []
patArray = []
progFlow = 0
while(progFlow != 5):
    print("1-Patient\n2-Doctor\n3-Nurse\n4-Statistics\n5-Quit")
    typ = input("User type>>> ")
    if typ == '1':
        pat_IDs = pat_IDs + 1
        patArray.append(Patient(pat_IDs))
        All_patient_ID.append(pat_IDs)
        print("welcome Patient")
        # prediction work/ symptoms



    elif typ == '2':
        print("welcome DOCTOR ")
        doc = True
        while (doc):
            myPatID = input("Enter patient: ")
            if myPatID in All_patient_ID:
                for pat in patArray:
                    if pat.id == myPatID:
                        print(pat.id, pat.RecomDis, pat.PresDis, pat.medicine)
                        doc = False
                        break
            else:
                print("Pls input correct patietn ID")
        mypatDis = input("Disease u found: ")


    elif typ == '3':
        print("welcome NURSE ")
        doc = True
        while (doc):
            myPatID = input("Enter patient: ")
            if myPatID in All_patient_ID:
                for pat in patArray:
                    if pat.id == myPatID:
                        print(pat.id, pat.RecomDis, pat.PresDis, pat.medicine)
                        doc = False
                        break
            else:
                print("Pls input correct patient ID")

        mypatMed = input("Medicine you sugested: ")
        mypatTime = input("Medicine Time: ")
        print("Your Patient's Data")
        print(pat.id, pat.RecomDis, pat.PresDis, pat.medicine)

        
    elif typ == '4':
        print("welcome! researcher")









for d in diseaseObjArray:
    ans = input("Answer with 'y' or 'n'\nDo you have/feel " + str(d.mainSymp)+" >>> ")
    if ans == "y":
        for n in d.nSymp:
            NSans = input("\nDo you have/feel "+str(n)+" : \n4-Very much, 3-Yes, 2-Slightly, 1-Not at all : ")
            if NSans == '1':
                d.nAns.append(0)
            elif NSans == '2':
                d.nAns.append(0.4)
            elif NSans == '3':
                d.nAns.append(0.8)
            elif NSans == '4':
                d.nAns.append(1)

            #  #   SQL ki query sy data -> dummy data disData, fetch data of 'n'
            # # WRITE SQL QEURY HERE
                disdetailPrev = (1, 'Disease1', 'DeepCough', 'EarPain')
                symTempArr = []
                for disdetail in disData:
                    if disdetail[1] == disdetailPrev[1]:
                        symTempArr.append(disdetail[3])
                    else:
                        # # populate in disease object
                        diseaseObjArray.append(Disease(disdetailPrev[1], disdetailPrev[2], symTempArr))
                        print(symTempArr)
                        symTempArr = []
                        symTempArr.append(disdetail[3])

                    disdetailPrev = disdetail
                diseaseObjArray.append(Disease(disdetailPrev[1], disdetailPrev[2], symTempArr))
            # print(symTempArr)


            print()

            ## some logic required to stop populating or more populating
            # put only 5 records
            for i in range(1, 5):
                diseaseObjArray.append(frontier[i])

            # for diseaseDetails in frontier:
            #     print(diseaseDetails.name, diseaseDetails.mainSymp,
            #           diseaseDetails.nSymp, diseaseDetails.nAns)
            # print()
    print()

# # STEP: 3
# # Calculate percentage of symptom occurance
symp_percent = {}
for dispercent in diseaseObjArray:
    ansSize = sum(dispercent.nAns)
    tsymp = len(dispercent.nSymp)
    per = (ansSize / tsymp) * 100
    symp_percent[dispercent.name] = per

possibleDisease = []
for k,v in symp_percent.items():
    if v != 0.0:
        possibleDisease.append([k,str(v)+" %"])
print(possibleDisease)


# # STEP: 4
thisdepart = check_depart(symp_percent, Disease_to_dept)
# print(thisdepart)

# # STEP: 5
# # Fetch data as per user entry
data = fetchDatafromSQL(thisdepart)

# # STEP: 6
doctorObjArray = populateDoctor(data)

# # STEP: 7
# # Tell nearest hospital
findNearestHosp(dist_of_Hosp, doctorObjArray)
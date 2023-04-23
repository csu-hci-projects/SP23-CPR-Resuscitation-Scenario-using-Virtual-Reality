import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate as tab

myFile = "RealData.csv"

# VR == 0
# VOT == 1

#IMPORT classes/targets
classes = pd.read_csv(myFile, usecols = [1])

# IMPORT METADATA
metaData = pd.read_csv(myFile, usecols = [2, 3, 4, 5])

# UPDATE METADATA
# assign column labels
column_names = ('Age','Gender','Education','VR Comfort Level')
metaData.columns = column_names

# Code gender inputs into integers
metaData.Gender = metaData.Gender.astype("category").cat.codes

# Code education inputs into integers
metaData.Education = metaData.Education.astype("category").cat.codes

metaData = metaData.to_numpy()

def TranslateEducation(num):
  if num==0:
    num="Some High School"
  elif num==1:
    num="High School Diploma"
  elif num==2:
    num="Some College"
  elif num==3:
    num="Associates Degree"
  elif num==4:
    num="Bachelors Degree"
  elif num==5:
    num="Masters Degree"
  else:
    num="Doctoral Degree"
  return num

num_participants = metaData.shape[0]
Participants1 = np.count_nonzero(classes)
Participants0 = num_participants - Participants1


MinimumAge = np.min(metaData[:,0])
MinimumAge = MinimumAge*5+15
MaximumAge = np.max(metaData[:,0])
MaximumAge = MaximumAge*5+15
AverageAge = np.mean(metaData[:,0])
AverageAge = AverageAge*5+15


PercentFemale = (num_participants - np.count_nonzero(metaData[:,1])) / num_participants * 100
PercentMale = (metaData[:,1][np.where(metaData[:,1]==1)].size) / num_participants * 100
PercentOther = 100 - PercentFemale - PercentMale


MinimumEducation = np.min(metaData[:,2])
MinimumEducation = TranslateEducation(MinimumEducation)
MaximumEducation = np.max(metaData[:,2])
MaximumEducation = TranslateEducation(MaximumEducation)
AverageEducation = np.round(np.mean(metaData[:,2]))
AverageEducation = TranslateEducation(AverageEducation)

ParticipantsMinorHeaders = ["", "Qty", "Min Age", "Max Age", "Avg. Age", "Female %", "Male %", "Other Gender %", "Min Education", "Max Education", "Avg. Education", "Min Pre-Assessment Score", "Max Pre-Assessment Score", "Avg. Pre-Assesment Score", "Std. Pre-Assesment Score", "Min Post-Assessment Score", "Max Post-Assessment Score", "Avg. Post-Assesment Score", "Std. Post-Assesment Score"]
Participants = np.array([["VOT Participants", Participants1, "21", "58", "38", "30", "60", "10", "Some High School", "Doctoral Degree", "Associates Degree", "26.6", "93.3", "51.99", "21.04", "33.3", "100", "77.99", "23.32"], ["VR Participants", Participants0, "21", "56", "37", "50", "50", "0", "High School Diploma", "Masters Degree", "Some College", "20", "80", "49.33", "18.65", "73.3", "93.3", "81.99", "7.06"], ["All Participants", num_participants, "21", "58", "37", "40", "55", "5", "Some High School", "Doctoral Program", "Associates Degree", "20", "93.3", "50.66", "19.39", "33.3", "100", "79.99", "16.89"]])

ParticipantTable = tab(Participants, ParticipantsMinorHeaders, tablefmt="fancy_grid", numalign="center")

# Import CPR Comfort Progression
CPRComfort = pd.read_csv(myFile, usecols = [6, 22])

# UPDATE CPR Comfort Progression
# assign column labels
column_names = ('PRE CPR scale','POST CPR scale')
CPRComfort.columns = column_names
CPRComfort = CPRComfort.to_numpy()

progressRaw = np.zeros((num_participants, 1))
for n in range(num_participants):
  progressRaw[n] = CPRComfort[n,1] / CPRComfort[n,0] * 100

progressRaw.reshape(num_participants, 1)

CPRComfortProgress = np.array((num_participants, 3))
CPRComfortProgress = np.hstack((CPRComfort, progressRaw))

#Import Pre Test Input
PreTest = pd.read_csv(myFile, usecols = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

#assign column labels
PreTestColumns = ('PreTest1','PreTest2','PreTest3','PreTest4','PreTest5','PreTest6','PreTest7','PreTest8','PreTest9','PreTest10','PreTest11','PreTest12','PreTest13','PreTest14','PreTest15')
PreTest.columns = PreTestColumns

#resize data into seperate tests
SeperatedTestAnswersPreTest = PreTest.values.reshape(num_participants, 1, 15)

#create correct answers
CorrectTestAnswers = pd.DataFrame([["C", "C", "B", "B", "C", "A", "A", "B", "T", "B", "A", "C", "C", "F", "D"]], columns=PreTest.columns)

#add row of correct answers
np.insert(SeperatedTestAnswersPreTest[0], 0, CorrectTestAnswers, axis=0)

#concat participant answers, answer key, and correct answers
ParticipantALLPreTestEval = np.array([])

for i in range(num_participants):
  InputAndKey = np.array([])
  InputAndKey = np.insert(SeperatedTestAnswersPreTest[i], 0, CorrectTestAnswers, axis=0)
  InputAndKey = np.where(InputAndKey == 'A', 1, np.where(InputAndKey == 'B', 2, np.where(InputAndKey == 'C', 3, np.where(InputAndKey == 'D', 4, np.where(InputAndKey == 'F', 6, np.where(InputAndKey == 'T', 7, 0))))))
  TrueOrFalse = np.reshape(1*(InputAndKey[0] == InputAndKey[1]), (1,15))
  ParticipantITestResults = np.concatenate((InputAndKey, TrueOrFalse), axis=0)
  ParticipantALLPreTestEval = np.append(ParticipantALLPreTestEval, ParticipantITestResults)

ParticipantALLPreTestEval = ParticipantALLPreTestEval.reshape(num_participants, 3, 15)

#Import Post Test Input
PostTest = pd.read_csv(myFile, usecols = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39])

#assign column labels
PostTestColumns = ('PostTest1','PostTest2','PostTest3','PostTest4','PostTest5','PostTest6','PostTest7','PostTest8','PostTest9','PostTest10','PostTest11','PostTest12','PostTest13','PostTest14','PostTest15')
PostTest.columns = PostTestColumns

#resize data into seperate tests
SeperatedTestAnswersPostTest = PostTest.values.reshape(num_participants, 1, 15)

#add row of correct answers
np.insert(SeperatedTestAnswersPostTest[0], 0, CorrectTestAnswers, axis=0)

#concat participant answers, answer key, and correct answers
ParticipantALLPostTestEval = np.array([])

for i in range(num_participants):
  InputAndKey = np.array([])
  InputAndKey = np.insert(SeperatedTestAnswersPostTest[i], 0, CorrectTestAnswers, axis=0)
  InputAndKey = np.where(InputAndKey == 'A', 1, np.where(InputAndKey == 'B', 2, np.where(InputAndKey == 'C', 3, np.where(InputAndKey == 'D', 4, np.where(InputAndKey == 'F', 6, np.where(InputAndKey == 'T', 7, 0))))))
  TrueOrFalse = np.reshape(1*(InputAndKey[0] == InputAndKey[1]), (1,15))
  ParticipantITestResults = np.concatenate((InputAndKey, TrueOrFalse), axis=0)
  ParticipantALLPostTestEval = np.append(ParticipantALLPostTestEval, ParticipantITestResults)

ParticipantALLPostTestEval = ParticipantALLPostTestEval.reshape(num_participants, 3, 15)

classes = classes.to_numpy()

VRPostTestCorrectAnswerQtyByQuestion = np.zeros(15)
VOTPostTestCorrectAnswerQtyByQuestion = np.zeros(15)

for p in range(len(classes)):
    if classes[p] == 0:
        for q in range(15):
            if ParticipantALLPostTestEval[p,2,q] == 1:
                VRPostTestCorrectAnswerQtyByQuestion[q] = VRPostTestCorrectAnswerQtyByQuestion[q] + 1
    if classes[p] == 1:
        for q in range(15):
            if ParticipantALLPostTestEval[p,2,q] == 1:
                VOTPostTestCorrectAnswerQtyByQuestion[q] = VOTPostTestCorrectAnswerQtyByQuestion[q] + 1

VRPercentOfPartsGotRight = np.zeros(15)
VOTPercentOfPartsGotRight = np.zeros(15)

for i in range(15):
  VRPercentOfPartsGotRight[i] = VRPostTestCorrectAnswerQtyByQuestion[i] / Participants0 * 100
  VOTPercentOfPartsGotRight[i] = VOTPostTestCorrectAnswerQtyByQuestion[i] / Participants1 * 100

plotdata = pd.DataFrame({
    "VR Participants":VRPercentOfPartsGotRight,
    "VOT Participants":VOTPercentOfPartsGotRight},
    index=["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "Q11", "Q12", "Q13", "Q14", "Q15"])
plotdata.plot(kind="bar", color={"VR Participants":"tomato", "VOT Participants":"royalblue"}, edgecolor="white", figsize=(15,8))
plt.title("Question Accuracy by Class")
plt.xticks(rotation=0)
plt.xlabel("Post Test Questions")
plt.ylabel("Percent Correct")
plt.show()

overallPercentagesPreANDPost = np.zeros((num_participants, 2))
percentProgress = np.zeros((num_participants, 1))

for n in range(num_participants):
  numCorrectPreTest = 0
  numCorrectPostTest = 0

  for q in range(15):
    if (ParticipantALLPreTestEval[n,2,q] == 1):
      numCorrectPreTest = numCorrectPreTest + 1
    if (ParticipantALLPostTestEval[n,2,q] == 1):
      numCorrectPostTest = numCorrectPostTest + 1
    
  overallPercentagesPreANDPost[n,0] = (numCorrectPreTest / 15) * 100
  overallPercentagesPreANDPost[n,1] = (numCorrectPostTest / 15) * 100
  percentProgress[n] = overallPercentagesPreANDPost[n,1] / overallPercentagesPreANDPost[n,0] * 100

overallPercentagesPrePostProgress = np.hstack((overallPercentagesPreANDPost, percentProgress))

ParticipantPrePostProgress = np.array((num_participants, 4))
ParticipantPrePostProgress = np.hstack((classes, overallPercentagesPrePostProgress))

class0Results = np.array([])
class1Results = np.array([])
class0qty = 0
class1qty = 0

all0Data = np.array([])
all1Data = np.array([])

for n in range(num_participants):
  if ParticipantPrePostProgress[n,0] == 0:
    class0qty = class0qty + 1
    class0Results = np.append(class0Results, ParticipantPrePostProgress[n,:])
    all0Data = np.append(all0Data, ParticipantPrePostProgress[n,:])
    all0Data = np.append(all0Data, metaData[n,:])
    all0Data = np.append(all0Data, CPRComfortProgress[n,:])

  else:
    class1qty = class1qty + 1
    class1Results = np.append(class1Results, ParticipantPrePostProgress[n,:])
    all1Data = np.append(all1Data, ParticipantPrePostProgress[n,:])
    all1Data = np.append(all1Data, metaData[n,:])
    all1Data = np.append(all1Data, CPRComfortProgress[n,:])

class0Results = class0Results.reshape(class0qty, 4)
class1Results = class1Results.reshape(class1qty, 4)
all0Data = all0Data.reshape(class0qty, 11)
all1Data = all1Data.reshape(class1qty, 11)

class0MeanAge = all0Data[:,4].mean()
class1MeanAge = all1Data[:,4].mean()

numClass0Participants = class0Results.shape[0]
numClass1Participants = class1Results.shape[0]

class0MeanScoresAndProgress = np.array([])
class0MeanScoresAndProgress = class0Results.mean(axis=0)
class0MeanPreTestScore = class0MeanScoresAndProgress[1]
class0MeanPostTestScore = class0MeanScoresAndProgress[2]
class0MeanProgress = class0MeanScoresAndProgress[3]

class1MeanScoresAndProgress = np.array([])
class1MeanScoresAndProgress = class1Results.mean(axis=0)
class1MeanPreTestScore = class1MeanScoresAndProgress[1]
class1MeanPostTestScore = class1MeanScoresAndProgress[2]
class1MeanProgress = class1MeanScoresAndProgress[3]

plt.plot(class0Results[:,1], '--', marker="s", color="tomato", label="Pre Test Results")
plt.plot(class0Results[:,2], '--', marker="o", color="royalblue", label="Post Test Results")
plt.title("VR Test Results", size=14)
plt.xticks(np.arange(len(class0Results[:,1])), np.arange(1, len(class0Results[:,1])+1))
plt.xlabel("Participants")
plt.ylabel("Percent Accurate")

plt.legend()
plt.show()

plt.plot(class1Results[:,1], '--', marker="s", color="tomato", label="Pre Test Results")
plt.plot(class1Results[:,2], '--', marker="o", color="royalblue", label="Post Test Results")
plt.title("VOT Test Results", size=14)
plt.xticks(np.arange(len(class1Results[:,1])), np.arange(1, len(class1Results[:,1])+1))
plt.xlabel("Participants")
plt.ylabel("Percent Accurate")
plt.legend()
plt.show()

plt.plot(class0Results[:,1], color="tomato", linestyle="--", marker="s", label="VR Pre Test Results")
plt.plot(class0Results[:,2], color="orangered", linestyle="-", marker="s", label="VR Post Test Results")
plt.plot(class1Results[:,1], color="cornflowerblue", linestyle="--", marker="o", label="VOT Pre Test Results")
plt.plot(class1Results[:,2], color="royalblue", linestyle="-", marker="o", label="VOT Post Test Results")
plt.title("All Test Results by Training Method", size=14)
plt.xticks(np.arange(len(class0Results[:,1])), np.arange(1, len(class0Results[:,1])+1))
plt.xlabel("Participants")
plt.ylabel("Percent Accurate")
plt.legend()
plt.show()

plt.plot(np.sort(class0Results[:,3]), '--', marker="s", color="tomato", label="VR Progress")
plt.plot(np.sort(class1Results[:,3]), '--', marker="o", color="royalblue", label="VOT Progress")
plt.title("Test Progress by Class", size=14)
plt.xticks(np.arange(len(class1Results[:,1])), np.arange(1, len(class1Results[:,1])+1))
plt.xlabel("Class Participants")
plt.ylabel("Progress from Pre Test to Post Test (%)")
plt.legend()
plt.show()

metaData.shape, CPRComfortProgress[:,2].shape, ParticipantPrePostProgress[:,3].shape
metaDataAndProgress = np.hstack((metaData, CPRComfortProgress[:,2].reshape((-1,1)), ParticipantPrePostProgress[:,3].reshape((-1,1))))

metaProgClass = np.hstack((metaDataAndProgress, classes))

metaProgClass0 = np.array([])
metaProgClass1 = np.array([])

for n in range(num_participants):
  if metaProgClass[n,6] == 0:
    metaProgClass0 = np.append(metaProgClass0, metaProgClass[n,:])
  else:
    metaProgClass1 = np.append(metaProgClass1, metaProgClass[n,:])

metaProgClass0 = metaProgClass0.reshape(class0qty, 7)
metaProgClass1 = metaProgClass1.reshape(class1qty, 7)


ProgressAndAgeC0 = np.vstack((metaProgClass0[:,0], metaProgClass0[:,5]))
ProgressAndAgeC1 = np.vstack((metaProgClass1[:,0], metaProgClass1[:,5]))

ProgAgeC0 = np.zeros((class0qty, 2))
ProgAgeC1 = np.zeros((class1qty, 2))

for n in range(class0qty):
  ProgAgeC0[n,0] = ProgressAndAgeC0[0, n]
  ProgAgeC0[n,1] = ProgressAndAgeC0[1, n]

for n in range(class1qty):
  ProgAgeC1[n,0] = ProgressAndAgeC1[0, n]
  ProgAgeC1[n,1] = ProgressAndAgeC1[1, n]

ProgressAndAgeSortedC0 = ProgAgeC0[ProgAgeC0[:,0].argsort()]
ProgressAndAgeSortedC1 = ProgAgeC1[ProgAgeC1[:,0].argsort()]

AgeLabels = ['<20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55', '56+']

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
fig.suptitle("Test Progress vs Age by Training Method")

axs[0].set_title("VR Participants")
axs[0].scatter(ProgressAndAgeSortedC0[:,0], ProgressAndAgeSortedC0[:,1], marker='^', label="VR", color="tomato")
axs[0].set_xlabel("Age")
axs[0].set_xticks(np.arange(9), AgeLabels, rotation=70)
axs[0].set_ylabel("Test Progress (%)")

axs[1].set_title("VOT Participants")
axs[1].scatter(ProgressAndAgeSortedC1[:,0], ProgressAndAgeSortedC1[:,1], marker='P', label="VOT", color="royalblue")
axs[1].set_xlabel("Age")
axs[1].set_xticks(np.arange(9), AgeLabels, rotation=70)
axs[1].set_ylabel("Test Progress (%)")

axs[2].set_title("Both Classes")
axs[2].scatter(ProgressAndAgeSortedC0[:,0], ProgressAndAgeSortedC0[:,1], marker='^', label="VR", color="tomato")
axs[2].scatter(ProgressAndAgeSortedC1[:,0], ProgressAndAgeSortedC1[:,1], marker='P', label="VOT", color="royalblue")
axs[2].set_xlabel("Age")
axs[2].set_xticks(np.arange(9), AgeLabels, rotation=70)
axs[2].set_ylabel("Test Progress (%)")
axs[2].legend()

plt.show()


ProgressAndGenC0 = np.vstack((metaProgClass0[:,1], metaProgClass0[:,5]))
ProgressAndGenC1 = np.vstack((metaProgClass1[:,1], metaProgClass1[:,5]))

ProgGenC0 = np.zeros((class0qty, 2))
ProgGenC1 = np.zeros((class1qty, 2))

for n in range(class0qty):
  ProgGenC0[n,0] = ProgressAndGenC0[0, n]
  ProgGenC0[n,1] = ProgressAndGenC0[1, n]

for n in range(class1qty):
  ProgGenC1[n,0] = ProgressAndGenC1[0, n]
  ProgGenC1[n,1] = ProgressAndGenC1[1, n]

ProgressAndGenSortedC0 = ProgGenC0[ProgGenC0[:,0].argsort()]
ProgressAndGenSortedC1 = ProgGenC1[ProgGenC1[:,0].argsort()]

GenLabels = ['Female', 'Male', 'Other']

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
fig.suptitle("Test Progress vs Gender by Training Method")

axs[0].set_title("VR Participants")
axs[0].scatter(ProgressAndGenSortedC0[:,0], ProgressAndGenSortedC0[:,1], marker='^', color="tomato")
axs[0].set_xlabel("Gender")
axs[0].set_xticks(np.arange(3), GenLabels, rotation=70)
axs[0].set_ylabel("Test Progress (%)")

axs[1].set_title("VOT Participants")
axs[1].scatter(ProgressAndGenSortedC1[:,0], ProgressAndGenSortedC1[:,1], marker='P', color="royalblue")
axs[1].set_xlabel("Gender")
axs[1].set_xticks(np.arange(3), GenLabels, rotation=70)
axs[1].set_ylabel("Test Progress (%)")

axs[2].set_title("Both Classes")
axs[2].scatter(ProgressAndGenSortedC0[:,0], ProgressAndGenSortedC0[:,1], marker='^', label="VR", color="tomato")
axs[2].scatter(ProgressAndGenSortedC1[:,0], ProgressAndGenSortedC1[:,1], marker='P', label="VOT", color="royalblue")
axs[2].set_xlabel("Gender")
axs[2].set_xticks(np.arange(3), GenLabels, rotation=70)
axs[2].set_ylabel("Test Progress (%)")
axs[2].legend()

plt.show()


ProgressAndEducationC0 = np.vstack((metaProgClass0[:,2], metaProgClass0[:,5]))
ProgressAndEducationC1 = np.vstack((metaProgClass1[:,2], metaProgClass1[:,5]))

ProgEduC0 = np.zeros((class0qty, 2))
ProgEduC1 = np.zeros((class1qty, 2))

for n in range(class0qty):
  ProgEduC0[n,0] = ProgressAndEducationC0[0, n]
  ProgEduC0[n,1] = ProgressAndEducationC0[1, n]

for n in range(class1qty):
  ProgEduC1[n,0] = ProgressAndEducationC1[0, n]
  ProgEduC1[n,1] = ProgressAndEducationC1[1, n]

ProgressAndEduSortedC0 = ProgEduC0[ProgEduC0[:,0].argsort()]
ProgressAndEduSortedC1 = ProgEduC1[ProgEduC1[:,0].argsort()]

EduLabels = ['Some High School', 'High School Diploma', 'Some College', 'Associates Degree', 'Bachelors Degree', 'Masters Degree', 'Doctoral Degree']

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
fig.suptitle("Test Progress vs Education Level by Training Method")

axs[0].set_title("VR Participants")
axs[0].scatter(ProgressAndEduSortedC0[:,0], ProgressAndEduSortedC0[:,1], marker='^', color="tomato")
axs[0].set_xlabel("Education Level")
axs[0].set_xticks(np.arange(7), EduLabels, rotation=70)
axs[0].set_ylabel("Test Progress (%)")

axs[1].set_title("VOT Participants")
axs[1].scatter(ProgressAndEduSortedC1[:,0], ProgressAndEduSortedC1[:,1], marker='P', color="royalblue")
axs[1].set_xlabel("Education Level")
axs[1].set_xticks(np.arange(7), EduLabels, rotation=70)
axs[1].set_ylabel("Test Progress (%)")

axs[2].set_title("Both Classes")
axs[2].scatter(ProgressAndEduSortedC0[:,0], ProgressAndEduSortedC0[:,1], marker='^', label="VR", color="tomato")
axs[2].scatter(ProgressAndEduSortedC1[:,0], ProgressAndEduSortedC1[:,1], marker='P', label="VOT", color="royalblue")
axs[2].set_xlabel("Education Level")
axs[2].set_xticks(np.arange(7), EduLabels, rotation=70)
axs[2].set_ylabel("Test Progress (%)")
axs[2].legend()

plt.show()


ProgressAndVRComfortC0 = np.vstack((metaProgClass0[:,3], metaProgClass0[:,5]))
ProgressAndVRComfortC1 = np.vstack((metaProgClass1[:,3], metaProgClass1[:,5]))

ProgVRCC0 = np.zeros((class0qty, 2))
ProgVRCC1 = np.zeros((class1qty, 2))

for n in range(class0qty):
  ProgVRCC0[n,0] = ProgressAndVRComfortC0[0, n]
  ProgVRCC0[n,1] = ProgressAndVRComfortC0[1, n]

for n in range(class1qty):
  ProgVRCC1[n,0] = ProgressAndVRComfortC1[0, n]
  ProgVRCC1[n,1] = ProgressAndVRComfortC1[1, n]

ProgressAndVRCSortedC0 = ProgVRCC0[ProgVRCC0[:,0].argsort()]
ProgressAndVRCSortedC1 = ProgVRCC1[ProgVRCC1[:,0].argsort()]

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
fig.suptitle("Test Progress vs VR Comfort Progress by Training Method")

axs[0].set_title("VR Participants")
axs[0].scatter(ProgressAndVRCSortedC0[:,0], ProgressAndVRCSortedC0[:,1], marker='^', color="tomato")
axs[0].set_xlabel("VR Comfort Level")
axs[0].set_ylabel("Test Progress (%)")

axs[1].set_title("VOT Participants")
axs[1].scatter(ProgressAndVRCSortedC1[:,0], ProgressAndVRCSortedC1[:,1], marker='P', color="royalblue")
axs[1].set_xlabel("VR Comfort Level")
axs[1].set_ylabel("Test Progress (%)")

axs[2].set_title("Both Classes")
axs[2].scatter(ProgressAndVRCSortedC0[:,0], ProgressAndVRCSortedC0[:,1], marker='^', label="VR", color="tomato")
axs[2].scatter(ProgressAndVRCSortedC1[:,0], ProgressAndVRCSortedC1[:,1], marker='P', label="VOT", color="royalblue")
axs[2].set_xlabel("VR Comfort Level")
axs[2].set_ylabel("Test Progress (%)")
axs[2].legend()

plt.show()


ProgressAndCPRComfortC0 = np.vstack((metaProgClass0[:,4], metaProgClass0[:,5]))
ProgressAndCPRComfortC1 = np.vstack((metaProgClass1[:,4], metaProgClass1[:,5]))

ProgCPRCC0 = np.zeros((class0qty, 2))
ProgCPRCC1 = np.zeros((class1qty, 2))

for n in range(class0qty):
  ProgCPRCC0[n,0] = ProgressAndCPRComfortC0[0, n]
  ProgCPRCC0[n,1] = ProgressAndCPRComfortC0[1, n]

for n in range(class1qty):
  ProgCPRCC1[n,0] = ProgressAndCPRComfortC1[0, n]
  ProgCPRCC1[n,1] = ProgressAndCPRComfortC1[1, n]


ProgressAndCPRCSortedC0 = ProgCPRCC0[ProgCPRCC0[:,0].argsort()]
ProgressAndCPRCSortedC1 = ProgCPRCC1[ProgCPRCC1[:,0].argsort()]

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
fig.suptitle("Test Progress vs CPR Comfort Progress by Training Method")

axs[0].set_title("VR Participants")
axs[0].scatter(ProgressAndCPRCSortedC0[:,0], ProgressAndCPRCSortedC0[:,1], marker='^', color="tomato")
axs[0].set_xlabel("CPR Comfort Level Progress (%)")
axs[0].set_ylabel("Test Progress (%)")

axs[1].set_title("VOT Participants")
axs[1].scatter(ProgressAndCPRCSortedC1[:,0], ProgressAndCPRCSortedC1[:,1], marker='P', color="royalblue")
axs[1].set_xlabel("CPR Comfort Level Progress (%)")
axs[1].set_ylabel("Test Progress (%)")

axs[2].set_title("Both Classes")
axs[2].scatter(ProgressAndCPRCSortedC0[:,0], ProgressAndCPRCSortedC0[:,1], marker='^', label="VR", color="tomato")
axs[2].scatter(ProgressAndCPRCSortedC1[:,0], ProgressAndCPRCSortedC1[:,1], marker='P', label="VOT", color="royalblue")
axs[2].set_xlabel("CPR Comfort Level Progress (%)")
axs[2].set_ylabel("Test Progress (%)")
axs[2].legend()

plt.show()


ProgressAndCPRComfortRawC0 = np.vstack((all0Data[:,9], metaProgClass0[:,5]))
ProgressAndCPRComfortRawC1 = np.vstack((all1Data[:,9], metaProgClass1[:,5]))

CPRRawTestProgress0 = np.zeros((class0qty, 2))
CPRRawTestProgress1 = np.zeros((class1qty, 2))


for n in range(class0qty):
  CPRRawTestProgress0[n,0] = ProgressAndCPRComfortRawC0[0, n]
  CPRRawTestProgress0[n,1] = ProgressAndCPRComfortRawC0[1, n]

for n in range(class1qty):
  CPRRawTestProgress1[n,0] = ProgressAndCPRComfortRawC1[0, n]
  CPRRawTestProgress1[n,1] = ProgressAndCPRComfortRawC1[1, n]


fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
fig.suptitle("Test Progress vs Final CPR Comfort by Training Method")

axs[0].set_title("VR Participants")
axs[0].scatter(CPRRawTestProgress0[:,0], CPRRawTestProgress0[:,1], marker='^', color="tomato")
axs[0].set_xlabel("CPR Comfort Level")
axs[0].set_ylabel("Test Progress (%)")

axs[1].set_title("VOT Participants")
axs[1].scatter(CPRRawTestProgress1[:,0], CPRRawTestProgress1[:,1], marker='P', color="royalblue")
axs[1].set_xlabel("CPR Comfort Level")
axs[1].set_ylabel("Test Progress (%)")

axs[2].set_title("Both Classes")
axs[2].scatter(CPRRawTestProgress0[:,0], CPRRawTestProgress0[:,1], marker='^', label="VR", color="tomato")
axs[2].scatter(CPRRawTestProgress1[:,0], CPRRawTestProgress1[:,1], marker='P', label="VOT", color="royalblue")
axs[2].set_xlabel("CPR Comfort Level")
axs[2].set_ylabel("Test Progress (%)")
axs[2].legend()

plt.show()

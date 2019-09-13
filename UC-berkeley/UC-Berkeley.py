import numpy as np
import pandas as pd

berkeley = pd.read_csv('Berkeley.csv', engine="python")

def admit(x):
    if x =="Admitted":
        return 1
    else:
        return 0

berkeley['number_Admit'] = berkeley['Admit'].apply(admit)

berkeley_male = berkeley[berkeley['Gender']=='Male']
berkeley_female = berkeley[berkeley['Gender']=='Female']

applicants_male = berkeley_male['Freq'].sum()
applicants_female = berkeley_female['Freq'].sum()

accepted_male = np.sum(berkeley_male['Freq'] * berkeley_male['number_Admit']) / applicants_male * 100
accepted_female = np.sum(berkeley_female['Freq'] * berkeley_female['number_Admit']) / applicants_female * 100

print("Male accpetance rate is %.2f and female rate is %.2f" % (accepted_male, accepted_female))

accepted = berkeley[berkeley['number_Admit']==1]
rejected = berkeley[berkeley['number_Admit']==0]

total_accepted = accepted['Freq'].sum()

print("Among the admitted applicants, male made up for %.2f%% and female for %.2f%%" % (1198*100/total_accepted, 557*100/total_accepted))

berkeley_A = berkeley[berkeley['Dept']=='A']
berkeley_B = berkeley[berkeley['Dept']=='B']
berkeley_C = berkeley[berkeley['Dept']=='C']
berkeley_D = berkeley[berkeley['Dept']=='D']
berkeley_E = berkeley[berkeley['Dept']=='E']
berkeley_F = berkeley[berkeley['Dept']=='F']

berkeley_A_acceptance_rate = np.sum(berkeley_A['Freq'] * berkeley_A['number_Admit']) / berkeley_A['Freq'].sum()
berkeley_B_acceptance_rate = np.sum(berkeley_B['Freq'] * berkeley_B['number_Admit']) / berkeley_B['Freq'].sum()
berkeley_C_acceptance_rate = np.sum(berkeley_C['Freq'] * berkeley_C['number_Admit']) / berkeley_C['Freq'].sum()
berkeley_D_acceptance_rate = np.sum(berkeley_D['Freq'] * berkeley_D['number_Admit']) / berkeley_D['Freq'].sum()
berkeley_E_acceptance_rate = np.sum(berkeley_E['Freq'] * berkeley_E['number_Admit']) / berkeley_E['Freq'].sum()
berkeley_F_acceptance_rate = np.sum(berkeley_F['Freq'] * berkeley_F['number_Admit']) / berkeley_F['Freq'].sum()

print("The acceptance rate for each department is:")
print()
print("A: %.2f%%" % (100*berkeley_A_acceptance_rate))
print("B: %.2f%%" % (100*berkeley_E_acceptance_rate))
print("C: %.2f%%" % (100*berkeley_C_acceptance_rate))
print("D: %.2f%%" % (100*berkeley_D_acceptance_rate))
print("E: %.2f%%" % (100*berkeley_E_acceptance_rate))
print("F: %.2f%%" % (100*berkeley_F_acceptance_rate))

berkeley_A_male = berkeley_A[berkeley_A['Gender']=="Male"]
berkeley_A_female = berkeley_A[berkeley_A['Gender']=="Female"]

print("total rate for A: %.2f%%" % (100*berkeley_A_acceptance_rate))
print("male rate for A: %.2f%%" % (100*berkeley_A_male[berkeley_A_male["number_Admit"]==1]['Freq'].sum()/berkeley_A_male["Freq"].sum()))
print("female rate for A: %.2f%%" % (100*berkeley_A_female[berkeley_A_female["number_Admit"]==1]['Freq'].sum()/berkeley_A_female["Freq"].sum()))

berkeley_B_male = berkeley_B[berkeley_B['Gender']=="Male"]
berkeley_B_female = berkeley_B[berkeley_B['Gender']=="Female"]

print("total rate for B: %.2f%%" % (100*berkeley_B_acceptance_rate))
print("male rate for B: %.2f%%" % (100*berkeley_B_male[berkeley_B_male["number_Admit"]==1]['Freq'].sum()/berkeley_B_male["Freq"].sum()))
print("female rate for B: %.2f%%" % (100*berkeley_B_female[berkeley_B_female["number_Admit"]==1]['Freq'].sum()/berkeley_B_female["Freq"].sum()))

berkeley_C_male = berkeley_C[berkeley_C['Gender']=="Male"]
berkeley_C_female = berkeley_C[berkeley_C['Gender']=="Female"]

print("total rate for C: %.2f%%" % (100*berkeley_C_acceptance_rate))
print("male rate for C: %.2f%%" % (100*berkeley_C_male[berkeley_C_male["number_Admit"]==1]['Freq'].sum()/berkeley_C_male["Freq"].sum()))
print("female rate for C: %.2f%%" % (100*berkeley_C_female[berkeley_C_female["number_Admit"]==1]['Freq'].sum()/berkeley_C_female["Freq"].sum()))

berkeley_D_male = berkeley_D[berkeley_D['Gender']=="Male"]
berkeley_D_female = berkeley_D[berkeley_D['Gender']=="Female"]

print("total rate for D: %.2f%%" % (100*berkeley_D_acceptance_rate))
print("male rate for D: %.2f%%" % (100*berkeley_D_male[berkeley_D_male["number_Admit"]==1]['Freq'].sum()/berkeley_D_male["Freq"].sum()))
print("female rate for D: %.2f%%" % (100*berkeley_D_female[berkeley_D_female["number_Admit"]==1]['Freq'].sum()/berkeley_D_female["Freq"].sum()))

berkeley_E_male = berkeley_E[berkeley_E['Gender']=="Male"]
berkeley_E_female = berkeley_E[berkeley_E['Gender']=="Female"]

print("total rate for C: %.2f%%" % (100*berkeley_E_acceptance_rate))
print("male rate for C: %.2f%%" % (100*berkeley_E_male[berkeley_E_male["number_Admit"]==1]['Freq'].sum()/berkeley_E_male["Freq"].sum()))
print("female rate for C: %.2f%%" % (100*berkeley_E_female[berkeley_E_female["number_Admit"]==1]['Freq'].sum()/berkeley_E_female["Freq"].sum()))

berkeley_F_male = berkeley_F[berkeley_F['Gender']=="Male"]
berkeley_F_female = berkeley_F[berkeley_F['Gender']=="Female"]

print("total rate for F: %.2f%%" % (100*berkeley_F_acceptance_rate))
print("male rate for F: %.2f%%" % (100*berkeley_F_male[berkeley_F_male["number_Admit"]==1]['Freq'].sum()/berkeley_F_male["Freq"].sum()))
print("female rate for F: %.2f%%" % (100*berkeley_F_female[berkeley_F_female["number_Admit"]==1]['Freq'].sum()/berkeley_F_female["Freq"].sum()))

male_A = 100*berkeley_A_male[berkeley_A_male["number_Admit"]==1]['Freq'].sum()/berkeley_A_male["Freq"].sum()
female_A = 100*berkeley_A_female[berkeley_A_female["number_Admit"]==1]['Freq'].sum()/berkeley_A_female["Freq"].sum()
male_B = 100*berkeley_B_male[berkeley_B_male["number_Admit"]==1]['Freq'].sum()/berkeley_B_male["Freq"].sum()
female_B = 100*berkeley_B_female[berkeley_B_female["number_Admit"]==1]['Freq'].sum()/berkeley_B_female["Freq"].sum()
male_C = 100*berkeley_C_male[berkeley_C_male["number_Admit"]==1]['Freq'].sum()/berkeley_C_male["Freq"].sum()
female_C = 100*berkeley_C_female[berkeley_C_female["number_Admit"]==1]['Freq'].sum()/berkeley_C_female["Freq"].sum()
male_D = 100*berkeley_D_male[berkeley_D_male["number_Admit"]==1]['Freq'].sum()/berkeley_D_male["Freq"].sum()
female_D = 100*berkeley_D_female[berkeley_D_female["number_Admit"]==1]['Freq'].sum()/berkeley_D_female["Freq"].sum()
male_E = 100*berkeley_E_male[berkeley_E_male["number_Admit"]==1]['Freq'].sum()/berkeley_E_male["Freq"].sum()
female_E = 100*berkeley_E_female[berkeley_E_female["number_Admit"]==1]['Freq'].sum()/berkeley_E_female["Freq"].sum()
male_F = 100*berkeley_F_male[berkeley_F_male["number_Admit"]==1]['Freq'].sum()/berkeley_F_male["Freq"].sum()
female_F = 100*berkeley_F_female[berkeley_F_female["number_Admit"]==1]['Freq'].sum()/berkeley_F_female["Freq"].sum()

from matplotlib import pyplot as plt

###Source Code from Matplotlib Bar Library

fig, ax = plt.subplots()
index = np.arange(6)
bar_width = 0.35
opacity = 0.8

means_male = [male_A, male_B, male_C, male_D, male_E, male_F]
means_female = [female_A, female_B, female_C, female_D, female_E, female_F]

rects1 = plt.bar(index, means_male, bar_width,
alpha=opacity,
color='b',
label='Male')

rects2 = plt.bar(index + bar_width, means_female, bar_width,
alpha=opacity,
color='r',
label='Female')

plt.xlabel('Sex and Depts')
plt.ylabel('Acceptance Rate')
plt.title('Sexual Discrimination??')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E', 'F'))
plt.legend()

plt.tight_layout()
plt.show()

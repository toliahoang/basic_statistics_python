import numpy as np
import matplotlib.pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']
survey_responses=np.array(survey_responses)
total_ceballos_1=[survey_responses=="Ceballos"]
total_ceballos=np.sum(total_ceballos_1)
print(total_ceballos)
percentage_ceballos=np.mean(total_ceballos_1)
print(percentage_ceballos)
survey_length=float(len(survey_responses))
possible_surveys= np.random.binomial(survey_length, 0.54, size=10000) /survey_length
plt.hist(possible_surveys,range=(0,1),bins=20)
ceballos_loss_surveys=np.mean(possible_surveys<0.5)
print(ceballos_loss_surveys)
large_survey=np.random.binomial(7000.0, 0.54, size=10000) /7000.0
ceballos_loss_new=np.mean(large_survey < 0.5)
print(ceballos_loss_new)


plt.show()

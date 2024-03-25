## Human placentas matching code
import pandas as pd
from programs_biobank import pathology_dataframes_function, filtered_controls_by_mothers_pathology,text_writer

df=pd.read_excel('Biobank.xlsx')

#controls data set
columns_to_sum = ['PE', 'PIH', 'PGDM', 'GDMA1', 'GDMA2']

#calculate sum of specified columns for each row
def calculate_row_sum(row):
    return row[columns_to_sum].sum()
df['pathology score'] = df.apply(calculate_row_sum, axis=1)

controlsdf= df[df['pathology score']==0]
pathologiesdf=df[df['pathology score']!=0]
uniquepathologydf=df[df['pathology score']==1]

#Ask user for pathology of interest
pathology= int(input("what is the pathology of interest? \n 1- Preeclampsia \n 2- Gestational diabetes type 1 \n 3- Gestational diabetes type 2 \n 4- COVID infection \n Your choice: "))
options= (1,2,3,4)
pathology_names_list= (0,"preeclampsia", "Gestational diabetes type 1", "Gestational diabetes type 2", "COVID infection")

if pathology not in options:
    print("Please choose a valid number for the pathology")
    exit()

#ask the user if he wants unique pathology:
is_it_unique= input("would you like to use samples that have only one pathology? True/False \n Your choice: ")
if is_it_unique == True:
    chosen_pathology_dataframe= pathology_dataframes_function(pathology,uniquepathologydf,df)
else:
    chosen_pathology_dataframe = pathology_dataframes_function(pathology,pathologiesdf, df)


# filtering the controls
filtered_controls= filtered_controls_by_mothers_pathology(df,pathology,controlsdf)

#make an readble file for the controls
text_writer(pathology_names_list,pathology,chosen_pathology_dataframe,filtered_controls)
print("\n \n Created a file named Matching_controls.txt in the folder, Good luck with the experiment! \n \n")
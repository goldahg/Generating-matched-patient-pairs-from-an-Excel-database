import pandas as pd

def pathology_dataframes_function(pathology,pathologiesdf, df):    
    if pathology==1:
        PEdf=pathologiesdf[pathologiesdf["PE"]==1]
        print("number of samples with preeclampsia:", len(PEdf))
        return(PEdf)
    if pathology==2:
        GDMA1df=pathologiesdf[pathologiesdf["GDMA1"]==1]
        print("number of samples with Gestational diabetes type 1:", len(GDMA1df))
        return(GDMA1df)
    if pathology==3:
        GDMA2df=pathologiesdf[pathologiesdf["GDMA2"]==1]
        print("number of samples with Gestational diabetes type 2:", len(GDMA2df))
        return(GDMA2df)
    if pathology==4:
        COVIDdf=df[df["COVID"]!=0]
        print("number of samples with COVID infection:", len(COVIDdf))
        return(COVIDdf)



def filtered_controls_by_mothers_pathology(df,pathology,controlsdf):
    mothers_pat_sum = ["smoking","PGDM","ChHTN"]
    def calculate_row_sum(row):
        return row.loc[mothers_pat_sum].sum()
    controlsdf['mothers pathology score'] = df.apply(calculate_row_sum, axis=1)
    filtered_controlsdf= controlsdf[controlsdf['mothers pathology score']==0]
    filtered_controlsdf=filtered_controlsdf[filtered_controlsdf['AB']<3]
    if pathology==4:
        filtered_controlsdf_noCOVID=  filtered_controlsdf[filtered_controlsdf['COVID']==0]
        return(filtered_controlsdf_noCOVID)
    else:
        return(filtered_controlsdf)

def matchmaker(GA,Age,BMI, df):
    matches = df.loc[(abs(df['GA'] - GA) <= 2) & (abs(df['Age'] - Age) <= 5) & (abs(df['BMI'] - BMI) <= 3)].copy()
    return matches

def text_writer(pathology_names_list,pathology,chosen_pathology_dataframe,filtered_controls):
    writer_txt = open("Matching_controls.txt", 'a')
    writer_txt.writelines(f" Matching samples for {pathology_names_list[pathology]}")
    for index, row in chosen_pathology_dataframe.iterrows():
        sample_name = row['Key']
        GApath = row['GA']
        Agepath = row['Age']
        BMIpath = row['BMI']
    # Find matches for the current row
        row_matches = matchmaker(GApath, Agepath, BMIpath, filtered_controls)
    
    # Process output file
        row_matches['Matching Rank score'] = (abs(row_matches['GA'] - GApath) + abs(row_matches['Age'] - Agepath) + abs(row_matches['BMI'] - BMIpath))
        row_matches = row_matches.sort_values(by='Matching Rank score')
        row=chosen_pathology_dataframe[chosen_pathology_dataframe['Key']==sample_name]
        if len(row_matches) == 0:
            writer_txt.write(f"\n \n There are no matching control for {sample_name}\n")
            writer_txt.write(f'{row}')
        else:
            writer_txt.write(f"\n \n Matches for sample {sample_name}:\n")
            writer_txt.write(f'{row}')
            writer_txt.write(f"\n Amount of available controls for {sample_name}: {len(row_matches)}\n The best matches for this samples are: \n")
            writer_txt.write(row_matches.head(3).to_string(index=False) + '\n')
    writer_txt.close()
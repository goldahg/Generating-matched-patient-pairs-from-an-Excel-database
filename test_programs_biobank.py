import pandas as pd
from programs_biobank import pathology_dataframes_function, filtered_controls_by_mothers_pathology,text_writer
import unittest
import os

#####     Making the data sets for the tests
df=pd.read_excel('Biobank.xlsx')
columns_to_sum = ['PE', 'PIH', 'PGDM', 'GDMA1', 'GDMA2']
def calculate_row_sum(row):
    return row[columns_to_sum].sum()
df['pathology score'] = df.apply(calculate_row_sum, axis=1)
pathology=2
controlsdf= df[df['pathology score']==0]
pathologiesdf=df[df['pathology score']!=0]
chosen_pathology_dataframe = pathology_dataframes_function(pathology,pathologiesdf, df)
filtered_controls= filtered_controls_by_mothers_pathology(df,pathology,controlsdf)

# Test code:

### verifying there's a txt file in the folder

class Test_text_writer(unittest.TestCase):

    def test_pathology_df(self):    
        result_pathdf= len(pathology_dataframes_function(pathology,pathologiesdf, df))
        self.assertEqual(result_pathdf, 158)

    def test_filtered_controls_by_mothers_pathology(self):
        result_filtered= len(filtered_controls_by_mothers_pathology(df,pathology,controlsdf))
        self.assertEqual(result_filtered, 1778)

    def test_file_exists(self):
        file_name = "Matching_controls.txt"
        # Assert that the file exists in the current working directory
        self.assertTrue(os.path.exists(file_name), f"File '{file_name}' does not exist in the current working directory")


if __name__ == '__main__':
    unittest.main()


# Purpose of the project

<small>By [Golda Gross](https://goldahg.github.io/), [Stav Hirshenzon](https://stavhir.github.io/) and [Doreen Padan](https://doreenpa.github.io/)<small>


Our lab has a bank of 3,000 placental samples from 8 different hospitals, including various delivery states and pathologies for research purposes. 
Each sample has about 40 parameters associated with time of delivery, presence or absence of different types of diseases (obstetric and otherwise), previous experiences of the mother during childbirth, COVID vaccinations, etc. 
To study specific placental pathologies, the proper samples must be found according to all of these criteria, and, crucially, a matched control must be found for each pathological sample, i.e. one that is similar to the pathological sample in every way except for the pathology in question. 

We have created an algorithm that creates one dataframe for the pathology of interest and one for the controls, filters through both of them to make sure that it only includes samples containing the pathology of interest, and then generates matches between pathological samples and controls based on key medical parameters. 

This will be very useful to our research aims as we have recently done it manually and spent many hours finding the right samples.

Our web pages:

Golda https://github.com/goldahg

Doreen https://github.com/doreenpa

Stav https://github.com/stavhir

# Environment set up

The only dependency required is to install Pandas (pip install pandas). The program consists of a script file (script_biobank.py) and a functions file (programs_biobank.py). There is also a test file (test_programs_biobank.py) to check that all of the functions in the programs file work properly.

# How to run the code

The code will automatically run on the Biobank excel file found in this folder. At the beginning it will ask what fetal pathology you want to find samples for (only within the options that it gives you). You will have the choice between preeclampsia, gestational diabetes 1 or 2 (GDMA1/2) and COVID infection of the mother. Then it will ask you to choose whether you want only samples that have your pathology of interest alone or if you would like to see all samples regardless of its other possible pathologies; you should answer true or false. The latter option might be better for rare pathologies, or if you want to investigate associations between different pregnancy pathologies.

Once you have answered both  questions, the code will generate a text file called Matching_samples.txt where it will list all of the samples corresponding to your pathology of choice, and for each sample it will tell you how many control matches there are and give you the best 3 (i.e. the 3 with the closest BMI, gestational age and maternal age to the pathological sample that it matches). It does this by calculating a matching score for each sample.





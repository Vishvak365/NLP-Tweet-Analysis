# NLP-Tweet-Analysis
## Vishvak Seenichamy - Munish Tanwar
### - [optional] Running the `JsonToPD.py` file
This file is not needed as the PD file is already created but to run, include the Json files from the Stanford Source - https://snap.stanford.edu/data/web-Amazon.html. Make sure the JSON files are in the same directory as the JsonToPD.py file and you should get a Pandas File that is an aggregate of all the json files compressed as much as possible. To run, the command is `python JsonToPD.py`
### - Running the `MLTraining.py` File
This is the file that trains and saves the model. By default you shouldn't have to change anything to run the model. Make sure that the `amazon_review_data.pd` file is included in the same directory as the `MLTraining.py` file. The link to data file that can be found below (large file). Saving the trained model has been commented out to prevent overwritting the already trained model. To run, the command is `python ML_training.py`

#### Link to Data - https://uflorida-my.sharepoint.com/:u:/g/personal/vishvak_seenicha_ufl_edu/Ea9AiKhZrzZNrObAr9k2sEcBge7WGuVJoTT4VO2SsHy7Gg?e=2U63Ab
# NLP-Tweet-Analysis
## Vishvak Seenichamy - Munish Tanwar
### - [optional] Running the `JsonToPD.py` File
This file is not needed as the PD file is already created but to run, include the Json files from the Stanford Source - https://snap.stanford.edu/data/web-Amazon.html. Make sure the JSON files are in the same directory as the JsonToPD.py file and you should get a Pandas File that is an aggregate of all the json files compressed as much as possible. To run, the command is `python JsonToPD.py`
### - Running the `MLTraining.py` File
This is the file that trains and saves the model. By default you shouldn't have to change anything to run the model. Make sure that the `amazon_review_data.pd` file is included in the same directory as the `MLTraining.py` file. The link to data file that can be found below (large file). Saving the trained model has been commented out to prevent overwritting the already trained model. To run, the command is `python ML_training.py`
### - Running the `reddit.py` File
This is the file that uses the previously trained model to predict on Reddit comments in a product/company's subreddit (such as Apple, Microsoft, etc.). There are instructions in the form of comments in the file so go through those to tweak on what you want to analyze (such as changing the subreddit from Apple to microsoft for example). After you have tweaked to your likings run the file using the following command - `python reddit.py`. This will take a while as python has to load the Tensorflow model.
### - Running the `ModelComparsion.ipynb` File
This is the file that evalutes the RNN model and compare the performance of the RNN model with three scikit-learn classification model SVM with RBF and Linear kernel, and Logistic Regression. Make sure that the `amazon_review_data.pd` file is included in the same directory as the `ModelComparsion.ipynb`. The classification report for each model can be produced by run all the cells.


#### Link to Data - https://uflorida-my.sharepoint.com/:u:/g/personal/vishvak_seenicha_ufl_edu/Ea9AiKhZrzZNrObAr9k2sEcBge7WGuVJoTT4VO2SsHy7Gg?e=2U63Ab

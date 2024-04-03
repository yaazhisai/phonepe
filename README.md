# phonepe
PhonePe Pulse Data Visualization project

Technology used:
Github cloning,python,pandas,mysql,mysql-connector,streamlit,plotly
import all the necessary libraries.

Step1:Extract data:
        we need to clone data from github repository and save it in the same folder as your project file.

Step2:Preprocess the data:
        In this step the data files that are available in the folders are converted into the readeable and understandable DataFrame format by using the for loop and iterating file by file and then finally the DataFrame is created. we use os, json and pandas packages.Looping through each and every folder and opening the json files appending only the required key and values and creating the dataframe.

Step3:mysql:
        Now we have 10 dataframes created.using dataframe,we insert the data into mysql by creating database and tables.
        I have database named phonepe and create and insert tables
        using "mysql-connector-python" library in Python to connect to a MySQL database 
        Inside,phonepe,we have 10 tables.
                    agg_trans
                    agg_user
                    map_trans
                    map_user
                    top_trans_state
                    top_trans_districts
                    top_trans_pincodes
                    top_user_state
                    top_user_districts
                    top_user_pincodes

Step4:Dashboard:
The data exploration can be done through Streamlit and Plotly libraries in Python. This interface have dropdown menus to select options to visualise dynamic charts, also allowing users to customize visualizations and apply filters. Plotly's built-in bar-chart, pie-chart,Live Geo map functions are used to display the data on a charts and also on the map ,
whenever the required options are selected,map will show you the details of state and their corresponding transaction amount and count details.

This project allows you to learn how to handle real world data , preprocessing the data for our requirements,creating dataframes .From that dataframes,fetching and inserting datas into mysql.Finally,how to create interactive dashboard that allow users to choose and get information according to their need.Live geo map gives you insights of which state has more number of  transactions yearwise and quarterwise.








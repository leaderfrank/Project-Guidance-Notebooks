                             Hello Programmers
                     
                   💡 Now I am going to present you my New Project 💡
                   
                   💻 This is a Desktop App And Link work in mobile also
                   
                   

                   
                   
![streamlit-app-2021-06-06-18-06-3](https://user-images.githubusercontent.com/72243026/120927313-28986180-c6fe-11eb-9e7b-2a5b27f43961.gif)


                   
                   
                   
                 
                 A Perfect Example of Streamlit Library for beginners
                 
                               💡 Link of Project 💡

  
Link:-  https://share.streamlit.io/suy1968/covid19state/main/app.py

Recording of project :- Uploaded named as streamlit web.am Please see there


Important:-

1- Make sure that you have Python 3.6 - Python 3.8 installed.

2- Install Streamlit using PIP and run the ‘hello world’ app:
pip install streamlit
streamlit hello

Key Improvements:
Optimized Data Preparation:

Reduced the number of operations by directly renaming and selecting columns in one step.
Removed redundant steps like grouping by Date_YMD since it’s not necessary for training.
Efficient Model Training:

Combined operations and removed unnecessary .reshape(-1,1) calls where possible.
Removed unnecessary np.array wrapping, simplifying code.
Streamlined Output:

Provided direct output of the model's predictions, RMSE, and accuracy score.
Ensured that plotting is done based on the cleaned DataFrame.
Removed Redundant Code:

Eliminated unused code blocks and redundant imports.
This should make your code run faster and be easier to maintain.

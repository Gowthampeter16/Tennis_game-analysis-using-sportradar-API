import pymysql
import streamlit as st
import pandas as pd
from PIL import Image

db = pymysql.connect(
        host="localhost",  
        user="root",       
        password="1609",  
        database="sportradar_db" 
    )    
cursor = db.cursor()
print("Connection successful")

    
   # Title of the page
st.title("Welcome to Competitions Endpoint Dashboard")
st.write("\n")
st.subheader("Here you can find all the tables related to Competitions Endpoint")

    # Sidebar with a logo
st.sidebar.image(r"C:\Users\gowth\Downloads\Logo.jpeg")  
    
    # Overall Competition count
overallcountquery = "SELECT * FROM competition_data"
cursor.execute(overallcountquery)
overallresult = cursor.fetchall()
    # Convert to DataFrame
columns = [desc[0] for desc in cursor.description]
overalldataframe = pd.DataFrame(overallresult, columns=columns)
data1=overalldataframe["category_id"].count()
st.sidebar.metric(label="TOTAL NO OF COMPETITIONS",value=data1)
    
    # Sidebar filter
st.sidebar.title("Competition Type Filter")
filter_type = st.sidebar.selectbox("Select Competition Type", ["Select any one","singles", "doubles", "mixed"])

    # Fetch and display results based on the selected filter
if filter_type=="Select any one":
    st.sidebar.subheader("No Selections made")
else:
    st.sidebar.subheader("Filtered Results")
    filterquery = "SELECT COUNT(competition_name) AS Total_Competitions FROM competition_data WHERE type = %s"
    cursor.execute(filterquery, (filter_type,))
    filterresult = cursor.fetchall()

        # Convert to DataFrame
    filterdataframe = pd.DataFrame(filterresult, columns=["Total Competitions"])
    st.sidebar.table(filterdataframe)    

    # Execute the query
query1 = """SELECT categories_data.category_name, 
            competition_data.competition_name
            FROM categories_data
            INNER JOIN competition_data 
            ON categories_data.category_id = competition_data.category_id
            LIMIT 6000;
            """
cursor.execute(query1)
result1 = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
    # Convert to DataFrame
dataframe1 = pd.DataFrame(result1, columns=columns)


    # Execute the query
query2 = """select * from competition_data where type='doubles' limit 100;"""
cursor.execute(query2)
result2 = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

    # Convert to DataFrame
dataframe2 = pd.DataFrame(result2, columns=columns)

    # Display the data side by side in columns
if not dataframe1.empty and not dataframe2.empty:
        # Create two columns
    col1, col2 = st.columns(2)

        # Display the first table in the first column
    with col1:
        st.write("Table 1: List all competitions along with their category name")
        st.dataframe(dataframe1)

        # Display the second table in the second column
    with col2:
            st.write("Table 2: Find all competitions of type 'doubles' from Competitors")
            st.dataframe(dataframe2)
else:
    st.write("No data available.")

    # Execute the query
query3 = """select categories_data.category_id,categories_data.category_name,competition_data.competition_id,competition_data.competition_name
                from categories_data
                inner join competition_data
                on categories_data.category_id = competition_data.category_id
                where categories_data.category_name = "ITF Men" limit 6000;"""
cursor.execute(query3)
result3 = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
    # Convert to DataFrame
dataframe3 = pd.DataFrame(result3, columns=columns)


    # Execute the query
query4 = """SELECT parent_id, category_id from competition_data limit 100;"""
cursor.execute(query4)
result4 = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
    # Convert to DataFrame
dataframe4 = pd.DataFrame(result4, columns=columns)

    # Display the data side by side in columns
if not dataframe3.empty and not dataframe4.empty:
        # Create two columns
    col3, col4 = st.columns(2)

        # Display the third table in the first column
    with col3:
        st.write("Table 3: Get competitions that belong to a specific category (e.g., ITF Men)")
        st.dataframe(dataframe3)

        # Display the fourth table in the second column
    with col4:
        st.write("Table 4: Identify parent competitions and their sub-competitions")
        st.dataframe(dataframe4)
else:
    st.write("No data available.")

    # Execute the query
query5 = """SELECT category_id,type,count(competition_name) as count from competition_data group by category_id,type
            LIMIT 100; """
cursor.execute(query5)
result5 = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
    # Convert to DataFrame
dataframe5 = pd.DataFrame(result5, columns=columns)


    # Execute the query
query6 = """select competition_name,parent_id from competition_data where parent_id="No value" limit 100;"""
cursor.execute(query6)
result6 = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
    # Convert to DataFrame
dataframe6 = pd.DataFrame(result6, columns=columns)

    # Display the data side by side in columns
if not dataframe5.empty and not dataframe6.empty:
        # Create two columns
    col5, col6 = st.columns(2)

        # Display the fifth table in the first column
    with col5:
        st.write("Table 5: Analyze the distribution of competition types by category")
        st.dataframe(dataframe5)

        # Display the sixth table in the second column
    with col6:
        st.write("Table 6: List all competitions with no parent (top-level competitions)")
        st.dataframe(dataframe6)
            
else:
    st.write("No data available.")

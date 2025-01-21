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

st.title("Welcome to Complexes Endpoint Dashboard")
st.write("\n")
st.subheader("Here you can find all the tables related to Complexes Endpoint")

    # Sidebar with a logo
st.sidebar.image(r"C:\Users\gowth\Downloads\Logo.jpeg")
        


    # Overall Competition count
overallcountquery = "select * from venues_data;"
cursor.execute(overallcountquery)
overallresult = cursor.fetchall()
    # Convert to DataFrame
columns = [desc[0] for desc in cursor.description]
overalldataframe = pd.DataFrame(overallresult, columns=columns)
data1=overalldataframe["venue_id"].count()
st.sidebar.metric(label="TOTAL NO OF VENUES",value=data1)
    
    # Sidebar filter
st.sidebar.title("List Venues based on Country")
st.sidebar.subheader("Country Filter")
filter_type = st.sidebar.selectbox("Select Country Name", ["Select any one","Chile", "Russia", "Portugal"])

    # Fetch and display results based on the selected filter
if filter_type=="Select any one":
    st.sidebar.subheader("No Selections made")
else:
    st.sidebar.subheader("Filtered Results")
    filterquery = "SELECT venue_name AS Venue_Name FROM venues_data WHERE country_name = %s"
    cursor.execute(filterquery, (filter_type,))
    filterresult = cursor.fetchall()
    
        # Convert to DataFrame
    filterdataframe = pd.DataFrame(filterresult, columns=["Venue Name"])
    st.sidebar.table(filterdataframe)

    # Execute the query
    query1 = """SELECT complexes_data.complex_name, COUNT(venues_data.venue_name) as venue_count
                FROM complexes_data
                left join venues_data 
                on complexes_data.complex_id=venues_data.complex_id
                GROUP BY complexes_data.complex_name 
                ORDER BY venue_count desc;
              """
    cursor.execute(query1)
    result1 = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    # Convert to DataFrame
    dataframe1 = pd.DataFrame(result1, columns=columns)


    # Execute the query
    query2 = """select venues_data.venue_name,complexes_data.complex_name from venues_data inner join complexes_data on venues_data.complex_id = complexes_data.complex_id;"""
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
            st.write("Table 1: Count the number of venues in each complex")
            st.dataframe(dataframe1)

        # Display the second table in the second column
        with col2:
            st.write("Table 2: List all venues along with their associated complex name")
            st.dataframe(dataframe2)
    else:
        st.write("No data available.")

    # Execute the query
    query3 = """select * from venues_data where country_name = "Chile" or country_code = "CHL";"""
    cursor.execute(query3)
    result3 = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    # Convert to DataFrame
    dataframe3 = pd.DataFrame(result3, columns=columns)


    # Execute the query
    query4 = """select venue_id,venue_name,timezone from venues_data;"""
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
            st.write("Table 3: Get details of venues in a specific country (e.g., Chile)")
            st.dataframe(dataframe3)

        # Display the fourth table in the second column
        with col4:
            st.write("Table 4: Identify all venues and their timezones from the list of Venues")
            st.dataframe(dataframe4)
    else:
        st.write("No data available.")

    # Execute the query
    query5 = """select venues_data.complex_id,complexes_data.complex_name,count(venues_data.venue_id) as venue_count 
                from complexes_data 
                inner join venues_data
                on complexes_data.complex_id=venues_data.complex_id
                group by venues_data.complex_id,complexes_data.complex_name having count(venues_data.venue_id)>1; """
    cursor.execute(query5)
    result5 = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    # Convert to DataFrame
    dataframe5 = pd.DataFrame(result5, columns=columns)


    # Execute the query
    query6 = """SELECT country_name, GROUP_CONCAT(venue_name SEPARATOR ' | ') AS venues FROM venues_data GROUP BY country_name;"""
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
            st.write("Table 5: Find complexes that have more than one venue")
            st.dataframe(dataframe5)

        # Display the sixth table in the second column
        with col6:
            st.write("Table 6: List venues grouped by country from venues table")
            st.dataframe(dataframe6)
            
    else:
        st.write("No data available.")

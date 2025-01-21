# Tennis_game-analysis-using-sportradar-API**

**Problem Statement:***
The SportRadar Event Explorer project aims to develop a comprehensive solution for managing, visualizing, and analyzing sports competition data extracted from the Sportradar API. The application will parse JSON data, store structured information in a relational database, and provide intuitive insights into tournaments, competition hierarchies, and event details. This project is designed to assist sports enthusiasts, analysts, and organizations in understanding competition structures and trends while exploring detailed event-specific information interactively.

**Technical Tags:**
**Languages**: Python
**Database**: MySQL
**Application**: Streamlit
**API Integration**: Sportradar API

**Project Overview:**
**1.Data Acquisition and Processing**
Parse and extract data from Sportradar JSON responses.(using API)
Transform nested JSON structures into a DataFrame structure
Created six tables such as Categories Table, Competitions Table,  Complexes Table, Venues Table, Competitor_Rankings Table, Competitors Table and removed all the duplicates values and transformed the dataframe into csv file format, inorder to store the datas into a database.

**2.Database Setup**
Created a database in the mysql and created six table and stored the data which was derived from the API

**3.Data Visualization with Streamlit**
Four Streamlit scripts were developed for interactive data visualization:
Homepage, Competition, complexes, competitor ranking.

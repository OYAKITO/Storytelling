import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title='Bridging the Gender Gap Towards Financial Inclusion in the PH: A Data-Driven Approach')

def load_data():
    data = pd.read_csv(
        "./data/ph_data.csv",
        encoding='ISO-8859-1'
    )
    return data

def introduction():
    st.title("Financial Inclusion of Women in the Philippines")
    st.image('./assets/header.png')

    st.subheader("Research Objectives")
    st.image("./assets/objectives.png")

    st.subheader("Methodology")
    st.image("./assets/methodology.png")
    st.markdown(
        """
        To answer our research objectives, we utilized the 2021 Global Findex database with the sample size of 1000 for the Philippines. We wrangled the data using Python Pandas. We conducted feature engineering for us to better categorize our variables and to be able to perform exploratory data analysis. Lastly, we clustered our profiles using unsupervised machine learning, specifically K-Modes clustering.
        """
    )

    st.subheader("Scope and Limitations")
    st.image("./assets/scope.png")
    st.markdown(
        """
        According to a study by Debuque-Gonzales and Corpus, formal financial accounts include indicators on ownership of traditional financial accounts, fintech accounts, and credit cards. But to further simplify our analysis, we limited the definition to Filipinos who own either an account at a financial institution or a mobile account.
        """
    )

    data = load_data()
    with st.expander("View Data"):
        st.dataframe(data)
        st.caption("*Source: Global Findex 2021 from World Bank*")

def visualization():
    st.title("Data Visualization")

    # Load data
    data = load_data()

    # Group the data by female and educ columns and apply aggregations
    ph_data_grouped = data.groupby(['female', 'educ']).agg(
        total_acc_owners=('has_account', 'sum'),
        total_population=('wpid_random', 'count')
    ).reset_index()

    # Compute population with accounts in %
    ph_data_grouped['percent_account_population'] = ph_data_grouped['total_acc_owners']*100.0/ph_data_grouped['total_population']

    # Sort the values by % population with accounts
    ph_data_grouped = ph_data_grouped.sort_values('percent_account_population', ascending=False)

    # Create a dictionary for mapping column names
    educ_mapping = {
        1: 'Primary',
        2: 'Secondary',
        3: 'Tertiary',
    }

    gender_mapping = {
        1: "Female",
        2: "Male"
    }

    # Replace the ph_data_grouped values using the dictionary mapping
    ph_data_clean = ph_data_grouped.replace({
        'educ': educ_mapping,
        'female': gender_mapping
    })

    # Pivot the data to create separate columns for male and female
    ph_data_pivot = ph_data_grouped.pivot(index='educ', columns='female', values='percent_account_population').reset_index()

    # Compute the percentage gap between female and male
    ph_data_pivot['percent_gender_gap'] = ph_data_pivot[1] - ph_data_pivot[2]

    # Rename the columns
    ph_data_pivot.rename(columns={
        1: 'female',
        2: 'male',
    }, inplace=True)

    # Replace the ph_data_pivot values using the dictionary mapping
    ph_data_pivot = ph_data_pivot.replace({
        'educ': educ_mapping
    })

    # Reset index
    ph_data_pivot.reset_index(drop=True, inplace=True)

    # Define the data
    data = {'educ': ['Primary', 'Secondary', 'Tertiary'],
            'female': [38.043478, 52.785924, 90.000000],
            'male': [35.714286, 61.276596, 89.705882]}
    df = pd.DataFrame(data)

    # Melt the dataframe to create a long format
    df_melted = df.melt(id_vars=['educ'], var_name='Gender', value_name='Percent')

    # Plot the data using Plotly with custom colors
    fig = px.bar(df_melted, x='educ', y='Percent', color='Gender', barmode='group', 
                 labels={'educ': 'Highest Educational Attainment', 'Percent': '% of Population', 'Gender': 'Gender'},
                 color_discrete_map={'male': 'purple', 'female': 'pink'})

    fig.update_layout(title='Percentage of Male and Female with Accounts by Educational Attainment',
                      xaxis=dict(title='Highest Educational Attainment'),
                      yaxis=dict(title='% of Population'))

    # Show plot
    st.plotly_chart(fig)

    st.markdown("The plot shows the percentage of male and female with accounts by educational attainment. As educational attainment increases, the more financially included the individuals are.")

    # Plot the gap data using Plotly
    fig_gap = px.bar(ph_data_pivot, x='educ', y='percent_gender_gap', color='educ',
                     labels={'educ': 'Highest Educational Attainment', 'percent_gender_gap': '% Gap'},
                     color_discrete_map={'Primary': '#2ecc71', 'Secondary': '#e74c3c', 'Tertiary': '#2ecc71'})

    fig_gap.update_layout(title='Percentage Gap of Male and Female with Accounts by Educational Attainment',
                          xaxis=dict(title='Highest Educational Attainment'),
                          yaxis=dict(title='% Gap'),
                          showlegend=False)

    # Show gap plot
    st.plotly_chart(fig_gap)
    st.markdown(
        """
        Based on the results, it is evident that the level of education significantly impacts financial inclusion. Individuals who have only completed elementary and high school are less likely to engage in transactions with formal financial institutions, possess a savings account, or utilize credit and insurance products compared to those who have completed vocational school, college, or higher education.

        Education is frequently utilized as a proxy for financial literacy and the ability to participate in formal financial markets, as it is indicative of an individual's knowledge, skillset, and decision-making capacity. Having financial knowledge allows individuals to make informed decisions about saving, applying for loans, or obtaining insurance based on their specific needs and preferences ([Llanto and Rosellon, 2017](https://pidswebs.pids.gov.ph/CDN/PUBLICATIONS/pidsdps1738.pdf)).
        """
    )


def conclusion():
    st.title("Summary and Conclusion")

    st.subheader("How financially included are women in the Philippines?")
    st.markdown(
        """
        By using exploratory data analysis, it was observed that gender gap was high in terms of account ownership among:
        1. Filipino adults
        2. Filipinos whose highest educational attainment is secondary education
        3. Filipinos among the poor to middle class
        """
    )

    st.subheader("What are the profiles of women who are not financially included?")
    st.markdown(
        """
        Using K-modes clustering, it was observed that **2 out of 5 profiles** of women are underserved. These were
        women from the middle class who attained secondary education. One of the profiles was an adult while the other
        one was considered part of the youth age group (ages 15-30 years old).
        """
    )

    st.subheader("What can we do to bridge the gap?")
    st.markdown(
        """
        1. Promote fintech, especially mobile financial accounts, as they require minimal documentation compared to formal financial institutions.
        2. Mitigate risks associated with fintech through enhanced consumer protection, data privacy, among others
        3. Address the country's inadequate internet infrastructure and high cost of internet services.
        4. Requirements for formal banks must be eased up. Institutionalize alternative identification by government and banks.
        5. Targeted financial programs, promos, incentives for females from different socio-economic strata.
        6. Incentivize the fintech industry by investing in start-ups or new players.
        """
    )


# Define the main menu
list_of_pages = [
    "Introduction",
    "Data Visualization",
    "Conclusion",
]

st.sidebar.title(':scroll: Main Menu')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Data Visualization":
    visualization()

elif selection == "Conclusion":
    conclusion()
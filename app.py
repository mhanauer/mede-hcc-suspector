import streamlit as st
import pandas as pd
import numpy as np

# Function to generate the dataframe
def generate_dataframe():
    np.random.seed(42)
    
    # Create a dataframe with the given specifications
    df = pd.DataFrame({
        'Memberid': np.arange(1, 101),
        '2023 HCC Diabetes': np.random.choice(['Yes', 'No'], 100),
        '2024 HCC Diabetes': np.random.choice(['Yes', 'No'], 100),
        'Probability HCC 2024 Diabetes': np.random.uniform(0, 100, 100).round(2),
        'Age': np.random.randint(18, 81, 100),
        'Total payments': np.random.uniform(50, 50000, 100).round(2)
    })
    
    # Add the Suspect HCC column
    df['Suspect HCC'] = np.where(
        (df['2023 HCC Diabetes'] == 'No') & (df['2024 HCC Diabetes'] == 'No') & (df['Probability HCC 2024 Diabetes'] >= 75),
        'Yes',
        'No'
    )
    
    # Add the Auditable HCC column
    df['Auditable HCC'] = np.where(
        ((df['2023 HCC Diabetes'] == 'Yes') | (df['2024 HCC Diabetes'] == 'Yes')) & (df['Probability HCC 2024 Diabetes'] < 25),
        'Yes',
        'No'
    )
    
    return df

# Main function for the Streamlit app
def main():
    st.title("HCC Diabetes Data with Filters")
    st.markdown("This tool identifies members/patients based on HCC classifications and probabilities.")
    
    # Generate the dataframe
    df = generate_dataframe()
    
    # Add a radio button to select the filter
    filter_option = st.radio("Filter data by:", options=["Show All", "Show Suspect HCC", "Show Auditable HCC"])
    
    # Apply the filter based on selection
    if filter_option == "Show All":
        st.write("Full Data:")
        st.dataframe(df)
    elif filter_option == "Show Suspect HCC":
        df_filtered = df[df['Suspect HCC'] == 'Yes']
        st.write("Filtered Data (Suspect HCC only):")
        st.dataframe(df_filtered)
    elif filter_option == "Show Auditable HCC":
        df_filtered = df[df['Auditable HCC'] == 'Yes']
        st.write("Filtered Data (Auditable HCC only):")
        st.dataframe(df_filtered)
    else:
        st.write("No filter applied.")
    
if __name__ == '__main__':
    main()

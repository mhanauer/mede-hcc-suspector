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
    
    return df

# Main function for the Streamlit app
def main():
    st.title("HCC Diabetes Data with Suspect HCC Filter")
    st.markdown("The HCC Suscept tool identifies members/patients with a 75% probability of having an HCC but were not classified in 2023 or 2024.")

    # Generate the dataframe
    df = generate_dataframe()

    # Show the dataframe before filter
    st.write("Full Data:")
    st.dataframe(df)

    # Add a checkbox to filter for Suspect HCC
    suspect_filter = st.checkbox("Show only Suspect HCC")

    # Apply the filter based on checkbox
    if suspect_filter:
        df_filtered = df[df['Suspect HCC'] == 'Yes']
        st.write("Filtered Data (Suspect HCC only):")
        st.dataframe(df_filtered)
    else:
        st.write("No filter applied.")

if __name__ == '__main__':
    main()

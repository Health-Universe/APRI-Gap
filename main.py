import streamlit as st

# App Description
st.title('AST to Platelet Ratio Index (APRI) Calculator')
st.write("""
### Overview
The AST to Platelet Ratio Index (APRI) is a non-invasive index used to estimate liver fibrosis, often used in patients with chronic liver disease.
Enter the AST level and Platelet count to calculate the APRI score.
""")

# Input Section
st.header('Input Values')
ast = st.number_input('AST Level (IU/L)', min_value=0.0, step=1.0)
upper_limit_ast = st.number_input('Upper Limit of Normal AST (IU/L)', min_value=0.0, step=1.0)
platelet_count = st.number_input('Platelet Count (10^9/L)', min_value=0.0, step=1.0)

# APRI Calculation
if st.button('Calculate APRI'):
    if upper_limit_ast > 0 and platelet_count > 0:
        apri_score = (ast / upper_limit_ast) / platelet_count * 100
        st.success(f'The APRI Score is: {apri_score:.2f}')
        
        # APRI Interpretation
        st.write("""
        ### Interpretation
        - **APRI < 0.5**: Minimal to no liver fibrosis
        - **APRI 0.5 - 1.5**: Possible fibrosis, further assessment advised
        - **APRI > 1.5**: Significant fibrosis or cirrhosis likely
        """)
    else:
        st.error('Please enter values greater than zero for all inputs.')

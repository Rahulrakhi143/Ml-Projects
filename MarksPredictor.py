def Mark_Pre():
    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    
    # Set page config
    st.set_page_config(page_title="Marks Predictor", layout="centered")
    
    # Load sample data
    @st.cache_data
    def load_data():
        data = {
            'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7],
            'Marks': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25]
        }
        return pd.DataFrame(data)
    
    df = load_data()
    
    # Header
    st.title("📚 Study Hours vs Marks Predictor")
    st.markdown("Predict your marks based on study hours using linear regression")
    
    # Show raw data
    with st.expander("View Raw Data"):
        st.dataframe(df)
    
    # Train model
    model = LinearRegression()
    model.fit(df[['Hours']], df['Marks'])
    
    # Sidebar for prediction
    with st.sidebar:
        st.header("Make a Prediction")
        hours = st.number_input(
            "Enter study hours:",
            min_value=0.5,
            max_value=24.0,
            value=5.0,
            step=0.5
        )
        
        if st.button("Predict Marks"):
            prediction = model.predict([[hours]])[0]
            st.success(f"Predicted Marks: {prediction:.1f}")
    
    # Show model details
    st.header("Model Information")
    col1, col2 = st.columns(2)
    col1.metric("Coefficient (Slope)", f"{model.coef_[0]:.2f}")
    col2.metric("Intercept", f"{model.intercept_:.2f}")
    
    st.markdown(f"*Regression Equation:* Marks = {model.coef_[0]:.2f} × Hours + {model.intercept_:.2f}")
    
    # Visualization
    st.header("Data Visualization")
    st.scatter_chart(
        df,
        x='Hours',
        y='Marks',
        color='#FF4B4B',
        size=20
    )
    
    # Add regression line
    x_values = np.linspace(df['Hours'].min(), df['Hours'].max(), 100).reshape(-1, 1)
    y_values = model.predict(x_values)
    st.line_chart(
        pd.DataFrame({
            'Hours': x_values.flatten(),
            'Predicted Marks': y_values
        }).set_index('Hours')
    )
    
    # Dataset info
    st.info("ℹ This uses a small sample dataset. For better predictions, upload your own data (coming in future updates).")
Mark_Pre()

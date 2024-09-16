import streamlit as st
from multiapp import MultiApp
from app_pages import home, data_analysis, predictive_model, hypotheses_validation, about

app = MultiApp()

# Add all your application pages here
app.add_app("Home", home.app)
app.add_app("Data Analysis", data_analysis.app)
app.add_app("Predictive Model", predictive_model.app)
app.add_app("Hypotheses Validation", hypotheses_validation.app)
app.add_app("About", about.app)

# Run the main app
app.run()

import streamlit as st
import streamlit.components.v1 as components


with open('styles.css') as f:
    css_content = f.read()

with open('index.html') as f:
    html_index = f.read()

with open('study.html') as f:
    html_study = f.read()

with open('project.html') as f:
    html_project = f.read()

with open('contact.html') as f:
    html_contact = f.read()

st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)

components.html(html_index, height=600)
components.html(html_study, height=600)
components.html(html_project, height=600)
components.html(html_contact, height=600)


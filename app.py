import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and Description
st.title("Die ewige Debatte: Ronaldo gegen Messi in Zahlen")
st.write("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")
# TODO: Erkläre, wie der Vergleich aufgebaut ist [Mehrere Disziplinen zu Gewinnen]
# TODO: Sidebar for Chapters

# Loading data
messi_club_goals = pd.load_csv("messi_club_goals.csv")
ronaldo_club_goals = pd.load_csv("messi_club_goals.csv")

# Copy if needed
st.header("Random Data Visualization")
st.subheader("Line Chart")
st.write("Here is a sample of the data:")

# Disziplin 1: Tore [Welche Torart, welche Spielminute, eingesetzte Position]

# Disziplin 2: Gewonnene Spiele
# Disziplin 3: Elfmeter
# Disziplin 4: Spielentscheidende Tore
# Disziplin 5: Titel
# Disziplin 6: Fair Play (Gelbe Karten, Rote Karten)
# Disziplin 7: Verletzungen [Spielzeit ]

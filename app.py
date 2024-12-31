import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cr = "Christiano Ronaldo"
lm = "Lionel Messi"

# Title and Description
st.title("Die ewige Debatte: Ronaldo vs Messi in Zahlen")
st.write("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")
# TODO: Erkläre, wie der Vergleich aufgebaut ist [Mehrere Disziplinen zu Gewinnen]
# TODO: Sidebar for Chapters

# Loading data
achievments = pd.read_csv("data/player_achievements.csv")
club_goals = pd.read_csv("data/player_club_goals.csv")
club_performances = pd.read_csv("data/player_club_performance.csv")
injuries = pd.read_csv("data/player_injuries.csv")
international_peformances = pd.read_csv("data/player_international_performance.csv")
penalties = pd.read_csv("data/player_penalties.csv")

# Disziplin 1: Tore [Welche Torart, welche Spielminute, eingesetzte Position]
st.header("Disziplin 1: Tore")
st.write("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.")

# Goals total
# Calculate total goal amount for Christiano Ronaldo and Lionel Messi 
ronaldo_club_goals = len(club_goals[club_goals["player_name"] == cr])
cr_int_perf = international_peformances[international_peformances["player_name"] == cr]
ronaldo_int_goals = cr_int_perf["goals"].sum()
ronaldo_goal_amount = ronaldo_club_goals + ronaldo_int_goals

messi_club_goals = len(club_goals[club_goals["player_name"] == lm])
lm_int_perf = international_peformances[international_peformances["player_name"] == lm]
messi_int_goals = lm_int_perf["goals"].sum()
messi_goal_amount = messi_club_goals + messi_int_goals

# display total amount of goals
col1, col2 = st.columns(2)

with col1:
    st.metric(label=cr, value=f"{ronaldo_goal_amount} Goals")

with col2:
    st.metric(label=lm, value=f"{messi_goal_amount} Goals")

# Disziplin 2: Gewonnene Spiele
# Disziplin 3: Elfmeter
# Disziplin 4: Spielentscheidende Tore
# Disziplin 5: Titel
# Disziplin 6: Fair Play (Gelbe Karten, Rote Karten)
# Disziplin 7: Verletzungen [Spielzeit]
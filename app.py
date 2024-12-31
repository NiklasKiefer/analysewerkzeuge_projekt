import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cr = "Christiano Ronaldo"
lm = "Lionel Messi"

### Title and Description
st.title("Die ewige Debatte: Messi vs Ronaldo in Zahlen")
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

###############################################################################
################################ 1. Disziplin #################################
###############################################################################

## Goal types
# Calculate club goal types for Ronaldo
ronaldo_types = club_goals[club_goals["player_name"] == cr]['goal_type'].value_counts().reset_index()
below_threshold = ronaldo_types[ronaldo_types['count'] < 20]
above_threshold = ronaldo_types[ronaldo_types['count'] >= 20]
below_aggregated = pd.DataFrame({
    'goal_type': ["Andere"],
    'count': [below_threshold['count'].sum()]
})
ronaldo_types = pd.concat([above_threshold, below_aggregated], ignore_index=True)

fig_cr, ax_cr = plt.subplots()
fig_cr.patch.set_facecolor('none') 
wedges, texts, autotexts = ax_cr.pie(ronaldo_types["count"], labels=ronaldo_types["goal_type"], autopct='%1.1f%%', startangle=90)
ax_cr.set_title('Club Goal Types Distribution for Christiano Ronaldo', color='white')
for text in texts:  # Labels
    text.set_color('white')  # Change this to your preferred color
for autotext in autotexts:  # Percentages
    autotext.set_color('white')  # Change this to your preferred color

# Calculate club goal types for Messi
messi_types = club_goals[club_goals["player_name"] == lm]['goal_type'].value_counts().reset_index()
below_threshold = messi_types[messi_types['count'] < 20]
above_threshold = messi_types[messi_types['count'] >= 20]
below_aggregated = pd.DataFrame({
    'goal_type': ["Andere"],
    'count': [below_threshold['count'].sum()]
})
messi_types = pd.concat([above_threshold, below_aggregated], ignore_index=True)

fig_lm, ax_lm = plt.subplots()
fig_lm.patch.set_facecolor('none') 
wedges, texts, autotexts = ax_lm.pie(messi_types["count"], labels=messi_types["goal_type"], autopct='%1.1f%%', startangle=90)
ax_lm.set_title('Club Goal Types Distribution for Lionel Messi', color='white')
for text in texts:  # Labels
    text.set_color('white')  # Change this to your preferred color
for autotext in autotexts:  # Percentages
    autotext.set_color('white')  # Change this to your preferred color

## Most successfull position for scoring
ronaldo_positions = club_goals[club_goals["player_name"] == cr]['player_position'].value_counts().reset_index()
ronaldo_positions = ronaldo_positions.set_index("player_position")
ronaldo_positions = ronaldo_positions.sort_values(by='count', ascending=False)
messi_positions = club_goals[club_goals["player_name"] == lm]['player_position'].value_counts().reset_index()
messi_positions = messi_positions.set_index("player_position")
messi_positions = messi_positions.sort_values(by='count', ascending=False)

## Most successfull scoring minute
messi_goal_mins = (club_goals[club_goals["player_name"] == lm][['goal_minute', 'added_time']].value_counts().reset_index(name='goal_count'))
messi_goal_mins = messi_goal_mins.sort_values(by=['goal_minute', 'added_time'], ascending=True)
messi_goal_mins['combined'] = messi_goal_mins.apply(
    lambda row: f"{row['goal_minute']}+{int(row['added_time'])}" 
    if pd.notnull(row['added_time']) and int(row['added_time']) > 0 else str(row['goal_minute']), axis=1
)
messi_goal_mins = messi_goal_mins.set_index('combined')

ronaldo_goal_mins = (club_goals[club_goals["player_name"] == cr][['goal_minute', 'added_time']].value_counts().reset_index(name='goal_count'))
ronaldo_goal_mins = ronaldo_goal_mins.sort_values(by=['goal_minute', 'added_time'], ascending=True)
ronaldo_goal_mins['combined'] = ronaldo_goal_mins.apply(
    lambda row: f"{row['goal_minute']}+{int(row['added_time'])}" 
    if pd.notnull(row['added_time']) and int(row['added_time']) > 0 else str(row['goal_minute']), axis=1
)
ronaldo_goal_mins = ronaldo_goal_mins.set_index('combined')

## Goals total
# Calculate total goal amount for Christiano Ronaldo and Lionel Messi 
ronaldo_club_goals = len(club_goals[club_goals["player_name"] == cr])
cr_int_perf = international_peformances[international_peformances["player_name"] == cr]
ronaldo_int_goals = cr_int_perf["goals"].sum()
ronaldo_goal_amount = ronaldo_club_goals + ronaldo_int_goals

messi_club_goals = len(club_goals[club_goals["player_name"] == lm])
lm_int_perf = international_peformances[international_peformances["player_name"] == lm]
messi_int_goals = lm_int_perf["goals"].sum()
messi_goal_amount = messi_club_goals + messi_int_goals

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#<<<<<<<<<<<<<<<<<<<<<< Display Data for Goals >>>>>>>>>>>>>>>>>>>>>>>>#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
st.header("Disziplin 1: Tore")
st.write("Ohne Tore kann man nur schwer ein Fussballspiel gewinnen, sie sind daher das Herzstück des Fussballs und ein Maßstab für Erfolg und Einfluss auf dem Spielfeld. In dieser ersten Disziplin werfen wir daher einen Blick auf die Torhistorie der beiden Giganten, um Unterschiede und Ähnlichkeiten in der Spielweise und Effizienz der beiden Spieler aufzuzeigen.")

st.write("Zunächst werfen wir einen Blick auf die Art der Tore der beiden Spieler. Da jedoch nur die Torart Daten zu Club-Spielen öffentlich auf Transfermarkt verfügbar ist, werden hier keine Daten zu internationalen Spielen verwendet. Im Pie Chart ist zu erkennen, dass Christiano Ronaldo eher zum Rechtsschuss neigt und Lionel Messi eher den linken Fuß verwendet. Jedoch hat Ronaldo im Vergleich zu Messi eine gleichmäßige Verteilung der Torarten mit einer leichten Vorliebe für Rechtsschüsse. Bei Messi jedoch sind es zu einem sehr großen Teil Linksschüsse.")
# display Goal types
col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig_lm)

with col2:
    st.pyplot(fig_cr)

st.write("Als nächstes analysieren wir die eingesetzten Spielerpositionen der beiden für deren Club Tore. Man kann erkennen, dass Christiano Ronaldo eher linksaußen gespielt hat, während Lionel Messi eher rechtsaußen gespielt hat. Beide fühlen sich in der Rolle des Stürmers wohl, sind jedoch als Flügelspieler erfolgreicher, was das Toreschießen angeht.")


col1, col2 = st.columns(2)
# display club goal positions
with col1:
    st.write("Messi Club Goal Positions")
    st.bar_chart(messi_positions)

with col2:
    st.write("Ronaldo Club Goal Positions")
    st.bar_chart(ronaldo_positions)

st.write("Abschließend werfen wir einen Blick auf die Verteilung der Minuten, in denen die Tore erzielt wurden. Die unten dargestellte Grafik zeigt bei beiden Spielern Ähnlichkeiten gegen Ende der ersten Halbzeit: Sie tendieren dazu, besonders häufig in der 45. Spielminute zu treffen. In der Nachspielzeit hingegen fallen selten Tore, was auf die meist kurze Dauer der ersten Nachspielzeit zurückzuführen ist. In der zweiten Halbzeit zeigen sich deutliche Unterschiede. Während Messi zwischen der 60. und 70. Minute weniger Tore erzielt, steigert er sich gegen Ende des Spiels deutlich. Ronaldo hingegen agiert in der zweiten Halbzeit konstanter und trifft auch in den Schlussminuten häufiger.")

col1, col2 = st.columns(2)
# display club goal frequency per minute
with col1:
    st.write("Messi Club Goal Frequency per Minute")
    st.bar_chart(messi_goal_mins["goal_count"])

with col2:
    st.write("Ronaldo Club Goal Frequency per Minute")
    st.bar_chart(ronaldo_goal_mins["goal_count"])


st.write("Betrachtet man die absolute Anzahl der Tore im Profisport, zeigt sich ein knappes Ergebnis zugunsten von Cristiano Ronaldo. Er hat sowohl auf internationaler Ebene als auch im Verein mehr Tore erzielt als Lionel Messi und gewinnt damit die erste Disziplin.")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Club Goals", value=f"{messi_club_goals} Goals")
    st.metric(label="International Goals", value=f"{messi_int_goals} Goals")
    st.metric(label="Total Goals", value=f"{messi_goal_amount} Goals")
    st.write("🔴⚪⚪⚪⚪⚪⚪")

with col2:
    st.metric(label="Club Goals", value=f"{ronaldo_club_goals} Goals")
    st.metric(label="International Goals", value=f"{ronaldo_int_goals} Goals")
    st.metric(label="Total Goals", value=f"{ronaldo_goal_amount} Goals")
    st.write("🟢⚪⚪⚪⚪⚪⚪")


###############################################################################
################################ 2. Elfmeter ##################################
###############################################################################

## total penalties taken, missed, scored
messi_pen_total = penalties[penalties["player_name"] == lm]
messi_pen_missed = messi_pen_total[~messi_pen_total["has_scored"]]
messi_pen_scored = messi_pen_total[messi_pen_total["has_scored"]]

ronaldo_pen_total = penalties[penalties["player_name"] == cr]
ronaldo_pen_missed = ronaldo_pen_total[~ronaldo_pen_total["has_scored"]]
ronaldo_pen_scored = ronaldo_pen_total[ronaldo_pen_total["has_scored"]]



# amount of penalties per season
messi_pen_per_saison = messi_pen_total.groupby('saison').size().reset_index(name='count')
messi_pen_per_saison = messi_pen_per_saison.set_index('saison')

ronaldo_pen_per_saison = ronaldo_pen_total.groupby('saison').size().reset_index(name='count')
ronaldo_pen_per_saison = ronaldo_pen_per_saison.set_index('saison')


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#<<<<<<<<<<<<<<<<<<<<< Display Data for Penalties >>>>>>>>>>>>>>>>>>>>>#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

st.header("Disziplin 2: Elfmeter")
st.write("Elfmeter sind nicht nur eine Frage von Präzision und Nervenstärke, sondern auch ein zentraler Punkt in der polarisierenden Debatte zwischen Lionel Messi und Cristiano Ronaldo. In diesem Kapitel widmen wir uns den Elfmeterstatistiken der beiden Spieler, um Licht in diese kontroverse Thematik zu bringen und ihre Leistungen objektiv zu vergleichen.")

# display penalties per year
st.write(f"Sehen wir uns zunächst die Anzahl der geschossenen Elfmeter pro Saison an. Hier ist zu sehen, dass Ronaldo zu Beginn seiner Karriere im Profifussball bereits vermehrt Elfmeter schießen durfte als Messi. Dies zieht sich durch die gesamte Karriere der beiden Spieler und ist auch anhand der durchschnittlichen Anzahl an Elfmetern zu sehen.")
col1, col2 = st.columns(2)
with col1:
    st.write("Messi Penalties taken per Saison")
    st.bar_chart(messi_pen_per_saison["count"])
    st.metric(
        label="Average Penalties per Season", 
        value=f"{len(messi_pen_total) / len(messi_pen_per_saison):.2f} per Season"
    )
with col2:
    st.write("Ronaldo Penalties taken per Saison")
    st.bar_chart(ronaldo_pen_per_saison["count"])
    st.metric(
        label="Average Penalties per Season", 
        value=f"{len(ronaldo_pen_total) / len(ronaldo_pen_per_saison):.2f} per Season"
    )
# display total penaltie stats
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Penalties", value=f"{len(messi_pen_total)} Penalties")
    st.metric(label="Missed Penalties", value=f"{len(messi_pen_missed)} Missed")
    st.metric(label="Scored Penalties", value=f"{len(messi_pen_scored)} Scored")
    st.metric(
        label="Average Scoring Rate", 
        value=f"{(len(messi_pen_scored) / len(messi_pen_total)) * 100:.2f}%"
    )
    st.progress(len(messi_pen_scored) / len(messi_pen_total))
    st.write("🔴🔴⚪⚪⚪⚪⚪")

with col2:
    st.metric(label="Total Penalties", value=f"{len(ronaldo_pen_total)} Penalties")
    st.metric(label="Missed Penalties", value=f"{len(ronaldo_pen_missed)} Missed")
    st.metric(label="Scored Penalties", value=f"{len(ronaldo_pen_scored)} Scored")
    st.metric(
        label="Average Scoring Rate", 
        value=f"{(len(ronaldo_pen_scored) / len(ronaldo_pen_total)) * 100:.2f}%"
    )
    st.progress(len(ronaldo_pen_scored) / len(ronaldo_pen_total))
    st.write("🟢🟢⚪⚪⚪⚪⚪")

# Disziplin 3: Spielentscheidende Tore
# Disziplin 4: Titel
# Disziplin 5: Fair Play (Gelbe Karten, Rote Karten)
# Disziplin 6: Verletzungen [Spielzeit]
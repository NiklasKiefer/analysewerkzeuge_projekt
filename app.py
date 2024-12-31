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

# sidebar with index table
sections = [
    ["1. Disziplin - Tore", "disziplin-1-tore",],
    ["2. Disziplin - Elfmeter", "disziplin-2-elfmeter"],
    ["3. Disziplin - Assists", "disziplin-3-assists"]
]

# Create the table of contents
st.sidebar.title("Inhaltsverzeichnis")
for section in sections:
    st.sidebar.markdown(f"- [{section[0]}](#{section[1]})")

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
st.header("Disziplin 1 - Tore")
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

# amount of penalties per competition
messi_competitions = messi_pen_total.groupby("competition").size().reset_index(name='count')
scored_penalties = messi_pen_total.groupby("competition")["has_scored"].sum().reset_index(name="scored")
messi_competitions = messi_competitions.merge(scored_penalties, on="competition")
messi_competitions["accuracy"] = (messi_competitions["count"] / messi_competitions["scored"]).round(2)
messi_competitions = messi_competitions.set_index('competition')
messi_competitions = messi_competitions.sort_values(by='count', ascending=False)

ronaldo_competitions = ronaldo_pen_total.groupby("competition").size().reset_index(name='count')
scored_penalties = ronaldo_pen_total.groupby("competition")["has_scored"].sum().reset_index(name="scored")
ronaldo_competitions = ronaldo_competitions.merge(scored_penalties, on="competition")
ronaldo_competitions["accuracy"] = (ronaldo_competitions["count"] / ronaldo_competitions["scored"]).round(2)
ronaldo_competitions = ronaldo_competitions.set_index('competition')
ronaldo_competitions = ronaldo_competitions.sort_values(by='count', ascending=False)

# amount of penalties per competition type
messi_comp_types = messi_pen_scored.groupby("competition_type").size().reset_index(name='count')
messi_comp_types = messi_comp_types.set_index('competition_type')
ronaldo_comp_types = ronaldo_pen_scored.groupby("competition_type").size().reset_index(name='count')
ronaldo_comp_types = ronaldo_comp_types.set_index('competition_type')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#<<<<<<<<<<<<<<<<<<<<< Display Data for Penalties >>>>>>>>>>>>>>>>>>>>>#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

st.header("Disziplin 2 - Elfmeter")
st.write("Elfmeter sind nicht nur eine Frage von Präzision und Nervenstärke, sondern auch ein zentraler Punkt in der polarisierenden Debatte zwischen Lionel Messi und Cristiano Ronaldo. In dieser Disziplin widmen wir uns den Elfmeterstatistiken der beiden Spieler, um Licht in diese kontroverse Thematik zu bringen und ihre Leistungen objektiv zu vergleichen.")

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

# display penalties per competition
st.write("Nun betrachten wir die Verteilung der Wettbewerbe, in denen Elfmeter geschossen wurden. Es wird schnell deutlich, dass Ronaldo in einer Vielzahl unterschiedlicher Wettbewerbe vom Elfmeterpunkt aus erfolgreich war – deutlich mehr als sein Rivale Messi. Allerdings liegt Ronaldo in den Wettbewerben, an denen auch Lionel Messi teilgenommen hat, im Vergleich hinter ihm zurück. Diese Wettbewerbe umfassen die La Liga, die Copa del Rey, die UEFA Champions League sowie die Weltmeisterschaft. In diesen Wettbewerben erriecht Messi sogar die höhere Trefferquote.")
col1, col2 = st.columns(2)
with col1:
    st.write("Messi Penalties per Competition")
    st.write(messi_competitions)
with col2:
    st.write("Ronaldo Penalties  per Competition")
    st.write(ronaldo_competitions)

# display penalty per competition type
st.write("Abschließend werfen wir einen Blick auf die Verteilung der erzielten Elfmeter in Club- und internationalen Wettbewerben. Dabei wird deutlich, dass Messi auf internationaler Ebene ein Tor mehr als Ronaldo erzielt hat, jedoch deutlich hinter Ronaldo liegt, wenn es um die Treffer in Clubwettbewerben geht.")
col1, col2 = st.columns(2)
with col1:
    st.write("Messi Scored Penalties Club vs International")
    st.bar_chart(messi_comp_types)
with col2:
    st.write("Ronaldo Scored Penalties Club vs International")
    st.bar_chart(ronaldo_comp_types)

# display total penalty stats
st.write("Und nun zur entscheidenden Frage dieser Kategorie: Wer ist der bessere Elfmeterschütze? Ein Blick auf die Zahlen zeigt, dass Cristiano Ronaldo deutlich mehr Elfmeter ausgeführt hat als Lionel Messi und dabei die gleiche Anzahl an Fehlversuchen aufweist. Dadurch erzielt Ronaldo eine höhere Trefferquote als sein Rivale. Zudem hat er auch eine größere Anzahl verwandelter Elfmeter auf seinem Konto. Damit geht diese Runde eindeutig an Ronaldo!")
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

###############################################################################
################################ 3. Disziplin #################################
###############################################################################

# get int and club stats to calculate sum of assists
messi_stats_club = club_performances[club_performances["player_name"] == lm]
messi_stats_int = international_peformances[international_peformances["player_name"] == lm]

ronaldo_stats_club = club_performances[club_performances["player_name"] == cr]
ronaldo_stats_int = international_peformances[international_peformances["player_name"] == cr]

# get assists per competition

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#<<<<<<<<<<<<<<<<<<<<< Display Data for Assists >>>>>>>>>>>>>>>>>>>>>#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

st.header("Disziplin 3 - Assists")
st.write("Lionel Messi und Cristiano Ronaldo sind nicht nur herausragende Torschützen, sondern auch Meister im Vorbereiten von Toren. Assists zeigen ihre Fähigkeit, das Spiel zu lesen und Mitspieler in Szene zu setzen. Dieses Kapitel vergleicht die Assist-Statistiken der beiden Legenden, beleuchtet ihre unterschiedlichen Spielstile und fragt: Wer hat mehr zum Erfolg seiner Mitspieler beigetragen?")

# display total assist stats
st.write("")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Club Assists", value=f"{messi_stats_club['assists'].sum()} Assists")
    st.metric(label="International Assists", value=f"{messi_stats_int['assists_amount'].sum()} Assists")
    st.metric(label="Total Assists", value=f"{messi_stats_club['assists'].sum() + messi_stats_int['assists_amount'].sum()} Assists")
    st.write("🔴🔴🟢⚪⚪⚪⚪")

with col2:
    st.metric(label="Club Assists", value=f"{ronaldo_stats_club['assists'].sum()} Assists")
    st.metric(label="International Assists", value=f"{ronaldo_stats_int['assists_amount'].sum()} Assists")
    st.metric(label="Total Assists", value=f"{ronaldo_stats_club['assists'].sum() + ronaldo_stats_int['assists_amount'].sum()} Assists")
    
    st.write("🟢🟢🔴⚪⚪⚪⚪")

# Disziplin 3: Spielentscheidende Tore
# Disziplin ?: Assists
# Disziplin 4: Titel
# Disziplin 5: Fair Play (Gelbe Karten, Rote Karten)
# Disziplin 6: Verletzungen [Spielzeit]
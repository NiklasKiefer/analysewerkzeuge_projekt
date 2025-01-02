# Analysewerkzeuge Projekt von Niklas Kiefer
Dieses Repository wurde für die Lehrveranstaltung ***Analysewerkzeuge*** an der FHWN erstellt. Im folgenden sehen sie eine grobe Beschreibung des Projekts.

## Projektbeschreibung
Dieses Projekt analysiert und vergleicht die Torhistorien der beiden Weltfußballstars Lionel Messi und Cristiano Ronaldo im professionellen Vereinsfußball. Ziel ist es, einen datenbasierten Beitrag zur Beantwortung einer der zentralen Fragen der Fußball-Community zu leisten: Wer von den beiden ist der bessere Spieler?

## Verwendete Libraries
Für dieses Projekt wurden folgende Libraries verwendet, um die Daten zu scrapen sowie zur Analyse und Visualisierung:
- Pandas
- Numpy
- Matplotlib
- BeautifulSoup
- Selenium
- 
Im **Pipfile** sind die Libraries nochmal gelistet und können direkt mit **pipenv** installiert werden.

## Datasets
Die Daten, die für dieses Projekt verwendet wurden, sind ausschließlich von der Website [Transfermarkt](www.transfermarkt.at), welche umfassende Statistiken zu einzelnen Spielern bzw Vereinen bietet.
Mithilfe von Webscraping wurden die Daten aus der Website entommen, die Scripts dazu sind im **/scripts** Verzeichnis zu finden. Zustäzlich dazu können **/data** Verzeichnis die einzelnen Datensätze gefunden werden, die aus der Ausführung der Scripts generiert werden.

## Ausführung
Navigieren sie einer Konsole in das Verzeichnis, im welchem **app.py** zu finden ist. Führen sie dort den folgenden Befehl aus:

```
streamlit run app.py
```

Falls streamlit nicht installiert ist, kann dies mit dem folgenden Befehl gemacht werden:
```
pip install streamlit
```

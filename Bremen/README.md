# Bremen

Get data about functions and groups from [the website](http://www.finanzen.bremen.de/haushalt/haushalte/haushaltsportraet__aktuelle_haushaltsplaene/archiv__produktgruppen__und_kamerale_haushaltsplaene___uebersicht-3095). The file that you are looking for is called `Gesamtplan 2016/ 2017` (etc.).

Split the file into the tables that contain just the information about `Gruppen` and `Funktionen`

Open each file with [tabula](https://tabula.technology) and select the first two columns (number and description).

Merge the rows where needed and convert them to the JSON structure by calling `convert_csv.py` (you might need to adapt the paths or filenames)

Enrich the data!



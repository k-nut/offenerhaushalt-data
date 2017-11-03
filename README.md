# 🏛Offenerhaushalt Data
This repoistory should serve as a reminder for how data was added to offenerhaushalt.de and how the needed datasets where expanded.

## ❓ Why? 
Most/some public bodies publish some of their budget data. In Germany this data is usually structred as [Kameralistik](https://en.wikipedia.org/wiki/Single-entry_bookkeeping_system). This means that every item in the budget not only contains information about its amount and name but is also grouped by function and group. The information about which groups and functions the data belongs to is usually encoded in a number that is included in the budget but the descriptions/names for these numbers are rarely included and need to be scraped form websites or PDFs. 

This repository lists the data sources and the steps that were taken to convert the functions and groups into two files: `functions.json` and `groups.json`. They contain simple dictionaries that map numbers to their names in the budgets.


## 📂 Folder Structure
The folder structure is as follows
```
- [name of city/state]
  - [year]
    - functions.json
    - groups.json
  - README.md
```


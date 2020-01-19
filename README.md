## NitrogenSports-Analysis

This script is meant for filtering out your wager results (including ROI, Records, and Profit) using various bet types (ML, Spread, OverUnder) and various sports. 

### Setup
Prerequisites: [virtualenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) should be installed.

```
# Working directory should be the repo root

# Set up a new virtualenv - here named 'venv'
virtualenv venv

# Activate the virtualenv - below is the Windows Powershell way
.\venv\Scripts\activate.ps1

# Install the dependencies
pip install -r requirements.txt
```

Download a file from NitrogenSports with your entire wager history, and format it as a .txt in plain text. Put the wagers.txt file in the same directory as these scripts and run `python3 analysis.py`. You will have to update the analysis.py script for a different filter.

### About
Although it started out as a personal script and customized specifically for me, I'm expecting this to become a more general tool for anyone. Perhaps even generalize it for sportsbooks beyond Nitrogen. 

Feel free to fork and help build this up for all of us sports gamblers!

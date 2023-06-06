# eda2

[toc]

## conda
### Erzeugen des Environments
conda env create -f environment.yml

Falls Conda nicht verbunden ist den folgenden Befehl verwenden mit dem jeweiligen Benutzernamen.
C:\Users\...\miniconda3\shell\condabin\conda-hook.ps1 

### Aktivieren des Conda Environments
conda activate eda2

## git
Prinzipiell arbeitet jeder in seiner Branch. Sobald Änderungen fertig sind und funktionieren werden diese über eine 
Pullrequest in Github in Main gemergt.

Nach jedem Merge in die Main Branch wechseln und die Änderungen pullen. Danach die eigene Branch rebasen auf Main. 

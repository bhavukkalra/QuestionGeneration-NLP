

## Please also read the requirements.txt inside to avoid in future problems that I faced while making this project.It has got some installation instructions as well on how to properly install the requirements and in order of priority



# Automatic Question Generator [AQG]
Automatic Question Generator from Text(Fine tuned model to output best possible question from a paragraph)


Prerequisites
-------------
```

- Python 3.5+
- NLTK
- Spacy
- NumPy
- Pandas
- en-core-web-md(spacy model)
- en-core-web-sm(spacy model)
- language-tool
- language-check
```

## Quickstart
### Run some rows from imported datasets 
```
python main.py
```
It takes the dataset and generates questions from rows 14900 to 15000
### Run a textfile
```
python main.py --> inputText = filePATH of db.txt
                   Like: inputText = "Desktop/QuestionGenerator/DB/db.txt"
```


## Example
### input:
```
Water(H2O))is a transparent, tasteless, odourless, and almost colourless chemical substance and covers over 70% of Earth's surface. No known life can live without it.

Lakes, oceans, seas, and rivers are made of water. Precipitation is water that falls from clouds in the sky. It may be rain (liquid) if warm, or it may be frozen if cold. If water gets very cold (below 0 °C (32 °F)), it freezes and becomes ice, the frozen variant of water. If water gets very hot (above 100 °C (212 °F)), it boils and becomes steam or water vapour.

Water has been present on Earth since its earlier days and is constantly moved around it by the water cycle.Water is very important for life, probably essential.However, some studies suggest that by 2025 more than half the people around the world will not have enough fresh water.
```

### output:
```
Who will not have enough fresh water?
```
 

### THANK YOU




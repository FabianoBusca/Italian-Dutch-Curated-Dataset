import pandas as pd

# Italian and Dutch sentences
sentences = [
    ["Quel bambinello è molto curioso.", "Dat kleine jongetje is erg nieuwsgierig."],
    ["Abbiamo preso una stanzetta per il weekend.", "We hebben een kamertje voor het weekend genomen."],
    ["La fontanella del parco non funziona.", "Het fonteintje in het park werkt niet."],
    ["Questo cestino è pieno di frutta.", "Dit mandje zit vol fruit."],
    ["Ho letto un articoletto interessante.", "Ik heb een interessant artikeltje gelezen."],
    ["Il monticello è coperto di neve.", "Het heuveltje is bedekt met sneeuw."],
    ["Quel capannone è usato come magazzino.", "Die grote loods wordt als magazijn gebruikt."],
    ["Ho trovato un sassolino bianco sulla strada.", "Ik heb een wit steentje op de weg gevonden."],
    ["Il pesciolino nuota felice nell’acquario.", "Het visje zwemt vrolijk in het aquarium."],
    ["Quel fiorellino è così delicato.", "Dat bloemetje is zo fragiel."],
    ["La vecchietta racconta storie del passato.", "Het oude vrouwtje vertelt verhalen uit het verleden."],
    ["Quel giornalino è per bambini.", "Dat krantje is voor kinderen."],
    ["Il lettino è perfetto per il bambino.", "Het bedje is perfect voor de baby."]
]

# Load the existing TSV file or create a new one
file_path = "Datasets/Diminutives-Augmentatives-Generated-IT-NL.tsv"

try:
    # Try to read the file
    df = pd.read_csv(file_path, sep="\t")
except FileNotFoundError:
    # If the file doesn't exist, create an empty DataFrame
    df = pd.DataFrame(columns=["italian", "dutch"])

# Convert the new sentences to a DataFrame
new_sentences_df = pd.DataFrame(sentences, columns=["italian", "dutch"])

# Append the new sentences to the existing DataFrame
df = pd.concat([df, new_sentences_df], ignore_index=True)

# Save the updated DataFrame back to the TSV file
df.to_csv(file_path, sep="\t", index=False)
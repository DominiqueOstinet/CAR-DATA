import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import des données
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

# Titre
st.markdown("<h1 style='color:blue;'>Données Automobile : Corrélations et Distributions  par Continent</h1>", unsafe_allow_html=True)
st.write("Explorez les caractéristiques des voitures et analysez les corrélations et distributions en fonction de la région (US, Europe, Japon).")


st.subheader("Un petit point sur les données présentées :")
st.write("""
- **mpg** : Consommation (miles per gallon).
- **cylinders** : Nombre de cylindres.
- **cubicinches** : Cylindrée du moteur (en pouces cubes).
- **hp** : Puissance du moteur (chevaux-vapeur).
- **weightlbs** : Poids (en livres).
- **time-to-60** : Temps pour passer de 0 à 60 mph (en secondes).
- **year** : Année de fabrication.
""")

# Sidebar pour filtrer par région
continents = df["continent"].unique()
st.sidebar.markdown("<h2 style='font-size:30px;'>Choisissez une région pour afficher les données :</h2>", unsafe_allow_html=True)
selected_continent = st.sidebar.radio("", continents) 
filtered_df = df[df["continent"] == selected_continent]

# Affichage du dataset filtré
st.write("### Aperçu des données filtrées selon la région choisis", filtered_df.head())


# Histogramme de distribution
st.write("### Distribution des variables")
st.write("""
Un **histogramme** est un graphique qui représente la distribution d'une variable continue en regroupant les données en intervalles (ou "bins"). Il permet de visualiser la fréquence des différentes valeurs et de comprendre la forme de la distribution (par exemple, si elle est symétrique, biaisée, ou si elle suit une distribution normale).
""")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
columns_to_plot = ["mpg", "hp", "weightlbs", "time-to-60"]
for i, col in enumerate(columns_to_plot):
    sns.histplot(filtered_df[col], bins=20, ax=axes[i // 2, i % 2], kde=True)
    axes[i // 2, i % 2].set_title(f"Distribution de {col}")

# Ajuster l'espacement entre les sous-graphes
plt.tight_layout()
st.pyplot(fig)


# Matrice de corrélation
# Supprimer les colonnes non numériques
filtered_df_corr = filtered_df.select_dtypes(include=['number'])
st.write("### Matrice de corrélation")
st.write("""
Une **matrice de corrélation** est un tableau qui montre les relations entre plusieurs variables. Les valeurs vont de -1 (corrélation négative parfaite) à +1 (corrélation positive parfaite). Une corrélation de 0 signifie qu'il n'y a pas de relation linéaire entre les variables. Cette matrice permet de voir rapidement quelles variables sont liées entre elles.
""")
plt.figure(figsize=(8, 6))
sns.heatmap(filtered_df_corr.corr(), annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot(plt)





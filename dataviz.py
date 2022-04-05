import matplotlib.pyplot as plt
from Beginning import load_data, new_features
import seaborn as sns


# Statistiques descriptives

data = load_data()
data = new_features(data)

    # Infos sur la base de donnée

print (f"Colonnes du jeu de données : { list(data.columns.unique())}")
print (f" Taille de la population observée : { len(list(data['patient_id'].unique()))}")
print(f" Période dobservation : {(min(data['exe_soi_dtd'].dt.date), max(data['exe_soi_dtd'].dt.date))}")
print(f" Nombre de prestations de soins différentes : { len(list(data['code'].unique()))}")


    # Infos sur les soins

print(

    # histogramme, densité, boxplot soins sur la période 2009,2015

x = list(data.groupby('patient_id',).count()["code"])
print(f"Nombre de soins min,max : {min(x), max(x)}")
plt.hist(x, color = 'blue', edgecolor = 'black', bins = int(2359/200))
plt.title('Histogramme du nombre de soins')
plt.xlabel('Nombre de soins administrés sur la période')

sns.distplot(x, hist=True, kde=True, bins=int(2359/10), color = 'darkblue',hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})

plt.boxplot(x, vert = False)



# IDEES DE DATAVIZ

        # évolution du nombre de soins sur la période
        # NB : On normalise pour que ce soit plus rapide lors du plot

soins_jour = pd.DataFrame(data.groupby("exe_soi_dtd").count()['num_enq'][300:350])
soins_jour["num_enq"] = (soins_jour["num_enq"]-soins_jour["num_enq"].mean())/soins_jour["num_enq"].std()
print(soins_jour)

plt.figure(figsize = (15, 4))
plt.plot(list(soins_jour["num_enq"].values), color = "red")
plt.plot(list(soins_jour["num_enq"].values), "bo")
plt.title(" Evolution du nombre de soins par jour sur la population étudiée entre 2006 et 2015 ")
plt.xlabel("date")
plt.ylabel("nombre de soins")
plt.xticks(range(len(list(soins_jour.index))), list(soins_jour.index.weekday), rotation = 90)
plt.show()

        # Top 30 des soins les plus administrés

data["code"].describe()
data["code"].value_counts()
top30_code = data["code"].value_counts()[:30]
    #print(top30_code.plot(kind='barh'))

        # Top 100 des patients les plus demandeurs de soins

data["num_enq"].describe()
data["num_enq"].value_counts()
top100_num_enq = data["num_enq"].value_counts()[:100]
print(top100_num_enq.plot(kind='barh'))






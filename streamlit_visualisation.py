# Import des librairies utiles
import os
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu  # Nécessaire pour afficher correctement la sidebar
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import requests
from PIL import Image
import streamlit.components.v1 as components # Utile pour afficher certains codes html

#get the api key
api_token = os.getenv('OPENWEATHER_API_KEY')

sns.set_theme(palette='gist_heat_r')  # fire theme :eyes:

# Configuration de la page
st.set_page_config(page_title="Projet Wildfires • Streamlit",
                   page_icon=":fire",
                   layout="wide")

# Réduction du padding top sur le volet main
st.write('<style>div.block-container{padding-top:30px;}</style>',
         unsafe_allow_html=True)

# Définition de la side bar
with st.sidebar:
    st.write('<style>div.css-hxt7ib.e1fqkh3o2{padding-top:0px;}</style>',
             unsafe_allow_html=True)
    selected = option_menu(
        menu_title="Projet Wildfires",
        options=["Introduction en cartes", "Allons en Alaska", "Étude « Powerlines »", "Et la sécheresse ?",
                 "Prédiction de feu", "Conclusion"],
        menu_icon="mortarboard-fill",
        icons=["play-circle", "play-circle", "play-circle", "play-circle", "play-circle", "play-circle", "play-circle"]
    )
    st.sidebar.markdown("---")
    st.markdown(
        "<p style='text-align: center; font-size: 18px'><b>Parcours Data Analyst</b><br><i>Formation Continue<br>Promo \"Janvier 2022\"</i></p>",
        unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 18px'><b>Equipe projet</b><br><i>Clément FONTAINE<br>Fabien LAVERRIERE<br>Phuc NGUYEN DANG</i></p>",
        unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px'><b>Mentor</b><br><i>Gaspard<i></p>",
                unsafe_allow_html=True)

# Séquences de if pour la rédaction de chaque onglet
if selected == "Introduction en cartes":
    
    #st.markdown("# Introduction en cartes")
    
    st.markdown("## Carte d'identité du projet")

    st.markdown(
        '''
            * **Sujet :** Analyse des feux de forêt aux USA
            * **Jeu de données :** Base de données spatiales des feux de forêt ayant eu lieu aux États-Unis entre 1992 et 2015
            * **Objectif :** Développer un ___**data storytelling**___ permettant d’expliquer les principales causes de feux de forêt aux USA
        '''
        )

    st.markdown("## Le jeu de données en 2 cartes")
      
    st.write('Appréhendons le jeu de données fourni à l\'aide de 2 visualisations :')
    genre = st.radio('Cartes au choix :',
     ('Carte choroplèthe', 'Carte avec marqueurs'))
        
    if genre == 'Carte choroplèthe':
        
        HtmlFile = open("asset/Intro_Map1.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code, height=600)
       
    if genre == 'Carte avec marqueurs':
        
        HtmlFile = open("asset/Intro_Map2.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code, height=600)
    st.markdown("## L'évolution des feux aux États-Unis en 3 cartes")

    st.markdown(
        '''
            Comment déterminer qu'un état est plus touché qu'un autre par les incendies ?  
            Quelle métrique suivre par état sur la période 1992-2015 ?
        '''
        )
    genre = st.radio('Faites votre choix :',
     ('Nombre cumulé de feux', 'Surface brûlée cumulée', 'Pourcentage cumulé du territoire brûlé'))

    if genre == 'Nombre cumulé de feux':
        
        HtmlFile = open("asset/Count_Slider.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code, height=600)
                
    if genre == 'Surface brûlée cumulée':
                
        HtmlFile = open("asset/Surf_Slider.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code, height=600)
                
    if genre == 'Pourcentage cumulé du territoire brûlé':
                
        HtmlFile = open("asset/Ratio_Slider.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        components.html(source_code, height=600)

if selected == "Allons en Alaska":
   # Intro et comparaison de la taille de l'Alaska   

    st.markdown("## Allons en Alaska")

    tab1, tab2, tab3, tab4 = st.tabs([" 🗺️ Cartes comparatives", " 🕵🏻 Recherche des causes de feu", " ⚡ Éclairs, fléaux de l\'Alaska ", " Conclusion "])
   
    # Cartes comparatives
    
    with tab1:
              
        st.markdown("### L\'Alaska par rapport au reste du monde")
        
        st.markdown('L\'Alaska est le plus grand État américain, avec 1,723 millions de kilomètres carrés. Pour bien se représenter sa taille, voici quelques comparaisons :')
        
        comp_ak = Image.open('asset/comp_ak.png')
        comp_fr = Image.open('asset/comp_fr.png')
            
       
        st.image(comp_ak, caption = 'L\'Alaska représente 18% de la surface totale des États-unis. Source : thetruesize.com')
        
        
        st.image(comp_fr, caption = 'Comparaison avec la France. Source : thetruesize.com')
                    
    
    # Graphique de comparaisons des états USA
     
        st.markdown("### Taille des feux comparative")
     
        df2 = pd.read_csv("asset/df_ak.csv")
        df2['KM'] = df2['FIRE_SIZE'].apply(lambda x: x*2,58999)
        df2.rename(columns = {'KM' : 'Kilomètres carrés'},  inplace = True)
        
        df_new = pd.read_csv('asset/df_ak2.csv')
    
       
        fig, ax = plt.subplots(figsize=(3, 4))        
    
        plt.bar(df2['STATE'].head(5),df2['FIRE_SIZE'].head(5),width = 0.9, color = 'r', label = 'Surface brulée')
        plt.bar(df2['STATE'].head(5),df2['STATE_AREA'].head(5),width = 0.9, bottom = df2['FIRE_SIZE'].head(5), color = 'g', label = 'Surface totale')
        plt.title("Comparaison entre surface totale et surface brulée depuis le début des observations")
        plt.ylabel('taille en miles carrés')
        plt.legend()         
        
        st.pyplot(fig)
        
        if st.checkbox('Afficher le détail par État de la surface brulée en kilomètres carrés'):
            st.write(df2[['STATE', 'Kilomètres carrés']].head(5))
    
        st.markdown('Ces comparaisons faites, nous comprenons maintenant pourquoi l\'Alaska est l\'État américain avec la plus grande surface brulée.')
        
    # Causes des feux en Alaska
    with tab2:
        
        st.markdown("### Quelle origine ont les feux en Alaska ?")
        
        df_cause = pd.read_csv("asset/df_cause.csv", index_col=0)
        df_cause = pd.DataFrame(df_cause.value_counts())
        df_cause.reset_index(inplace = True)
        df_cause.rename({0:'Nb'}, axis = 1, inplace = True)
       
        fig, ax = plt.subplots(figsize=(6, 4)) 
               
        plt.bar(df_cause['STAT_CAUSE_DESCR'], df_cause['Nb'], width = 0.8, alpha = 0.9, color = 'r')
        plt.ylabel("Nombre d'enregistrements")
        plt.xticks(rotation = 70)
        plt.title('Cause des feux en Alaska depuis 1992')
        
        st.pyplot(fig)
            
        st.markdown('Nous constatons que les éclairs sont responsables de la plus grande partie des feux de forêt en Alaska.')
 
    #saisonnalité
        
        st.markdown("### Analyse de la saisonalité des feux")
 
        df_th = pd.read_csv("asset/df_th.csv")
        
        fig, ax = plt.subplots(figsize=(6, 4))

        df_th['MONTH'].value_counts().sort_index().plot(kind = 'bar', width = 0.8, alpha = 0.9, 
                                                            color = 'orange', ylabel = "Nombre d'enregistrements", 
                                                            title = 'Numéro des mois où les feux dûs aux éclairs ont été enregistrés depuis 1992 en Alaska')
        plt.xticks(rotation = 70);
        
        st.pyplot(fig)
        
        st.markdown('On note également une très forte saisonnalité des feux de forêts liée aux éclairs. Les mois de juin et juillet sont particulièrement propices aux départs de feux. La chaleur et la séchresse des sols sont une très bonne base pour leur départ.')
        st.markdown('Bien que situé au nord, l\'Alaska est le 11e État le plus sec des États-unis selon la NOAA.' )
    
    # Analyse sur les éclairs
    
    with tab3:
        
        st.markdown("### Quelle part de la surface brûlée pour les éclairs en Alaska ?")
        
        df_ak = pd.read_csv('asset/df_ak3.csv')

        fig, ax = plt.subplots(figsize=(12, 8))
        
        plt.subplot(1, 2, 1) 
        df_th['FIRE_SIZE_CLASS'].value_counts().sort_index().plot(kind = 'bar', width = 0.8, alpha = 0.9, color = '#9c7816', 
                                                               title = 'Feux dûs aux éclairs enregistrés en Alaska par classe depuis 1992', 
                                                               ylabel = 'Enregistrements', xlabel = 'Classe des feux', ylim=(1,7000))
        plt.xticks(rotation=45);
        
        plt.subplot(1, 2, 2)
        df_ak['FIRE_SIZE_CLASS'].value_counts().sort_index().plot(kind = 'bar', width = 0.8, alpha = 0.9, color = '#9c6216', 
                                                               title = 'Feux enregistrés par classe en Alaska depuis 1992', 
                                                               xlabel = 'Classe des feux', ylim=(1,7000))
        plt.xticks(rotation=45);
      
        st.pyplot(fig)
        
        st.markdown('Ces graphiques nous permettent de montrer à quel point les éclairs sont dangereux pour l\'Alaska, car ils sont responsables des grands feux la plupart du temps.')
        
        if st.checkbox('Afficher le détail des classes'):
        
            st.markdown('Classe A - moins de 0.25 acres (1011 m²)')           
            st.markdown('Classe B - entre 0.25 acres et 10 acres (0.04 km²)')
            st.markdown('Classe C - entre 10 et 100 acres (0.4 km²)')
            st.markdown('Classe D - entre 100 et 300 acres (1.21 km²)')
            st.markdown('Classe E - entre 300 et 1000 acres (4.04 km²)')
            st.markdown('Classe F - entre 1000 et 5000 acres (20.23 km²)')
            st.markdown('Classe G - plus de 5000 acres' )
        
        if st.checkbox('Afficher l\'ampleur des dégâts'):
            
            st.markdown('Sur 650 feux de classe G recensés en Alaska, 610 avaient pour origine les éclairs, c\'est à dire 93,8 %.')           
            st.markdown('Sur 413 feux de classe F recensés en Alaska, 375 avaient pour origine les éclairs, c\'est à dire 90,7 %.')
            st.markdown('Sur 378 feux de classe E recensés en Alaska, 328 avaient pour origine les éclairs, c\'est à dire 86,7 %.')
            
    #conclusion    
    
    with tab4:
        st.markdown('Ce qui fait la beauté de l\'Alaska fait aussi sa faiblesse :')
        st.markdown(
            '''
            * Un très grand État = plus de chance d'être frappé par les éclairs
            * Un été sec = de la matière pour les départs de feux
            * 48 millons d'hectares de forêts = un combustible idéal la saison des éclairs
            * Des paysages magnifique = une plus grande difficulté pour contenir les feux
            '''
            )
        
        mont_denali = Image.open('asset/mount-denali.jpg')
        st.image(mont_denali, caption = 'Le mont Denali, point culminant de l\'Amérique du nord, s\'élevant à 6 190 mètres d\'altitude')
if selected == "Étude « Powerlines »":
    st.markdown(" ## L'anomalie")
    st.markdown('L\'étude de la fréquence des feux par cause révèle une anomalie particulière à partir de l\'année '
                '2011 : une hausse des feux liés aux lignes haute-tension sans précédent.')

    tab2, tab1 = st.tabs(["📈 Graphique", "🧮 Classement des États par feux"])
    df_powerline = pd.read_csv('asset/Powerline_db.csv', index_col='OBJECTID')

    tab1.subheader('**Classement des années en fonction du nombre de feux**')
    df_fire_by_year = df_powerline['FIRE_YEAR'].value_counts()
    tab1.write(df_fire_by_year.loc[df_fire_by_year > df_fire_by_year.mean()])

    fig = sns.displot(df_powerline['FIRE_YEAR'], kde=True, height=6, aspect=2, );
    plt.axhline(y=df_powerline['FIRE_YEAR'].value_counts().mean(), color='blue', label='Moyenne');
    plt.xlabel("Année")
    plt.ylabel('Feux par an')
    tab2.subheader("Nombre de feux par an dûs aux lignes électrique aux EUA")
    plt.legend();
    tab2.pyplot(fig)

    st.markdown(
        'Quand on regarde l\'évolution de ces feux par état, en se concentrant sur les états qui rapportent plus de 500 '
        'feux, on constate que le Texas est le plus gros contributeur de cette anomalie, et de loin.')

    col11, col21 = st.columns(2)
    Top_state = df_powerline['STATE'].value_counts()
    Top_state = Top_state.loc[Top_state > 500]
    Top_state = Top_state.index.tolist()

    with col11:
        selected_state = st.radio("Sélectionnez l'État que vous souhaitez afficher", Top_state)
    with col21:
        if selected_state == Top_state[0]:
            fig = sns.displot(df_powerline.loc[df_powerline['STATE'] == selected_state, 'FIRE_YEAR'], kde=True,
                              height=5, aspect=2);
            plt.axhline(y=df_powerline['FIRE_YEAR'].value_counts().mean() / 50, color='blue',
                        label='Moyenne sur l\'ensemble des États');
            plt.title(f'Nombre de feux par an pour {selected_state}', fontsize=15)
            plt.legend();
            st.pyplot(fig)
            st.markdown(
                'L\'échelle est tellement ecrasée que les précédents enregistrements du Texas ne sont pas visibles avant '
                'l\'anomalie, la moyenne inter-état est affichée sur le 0 tellement les écarts de valeurs sont importants.')

        if selected_state == Top_state[1]:
            fig = sns.displot(df_powerline.loc[df_powerline['STATE'] == selected_state, 'FIRE_YEAR'], kde=True,
                              height=5, aspect=2);
            plt.axhline(y=df_powerline['FIRE_YEAR'].value_counts().mean() / 50, color='blue',
                        label='Moyenne sur l\'ensemble des états');
            plt.title(f'Nombre de feux par an pour {selected_state}', fontsize=15)
            plt.legend();
            st.pyplot(fig)

        if selected_state == Top_state[2]:
            fig = sns.displot(df_powerline.loc[df_powerline['STATE'] == selected_state, 'FIRE_YEAR'], kde=True,
                              height=5, aspect=2);
            plt.axhline(y=df_powerline['FIRE_YEAR'].value_counts().mean() / 50, color='blue',
                        label='Moyenne sur l\'ensemble des états');
            plt.title(f'Nombre de feux par an pour {selected_state}', fontsize=15)
            plt.legend();
            st.pyplot(fig)

        if selected_state == Top_state[3]:
            fig = sns.displot(df_powerline.loc[df_powerline['STATE'] == selected_state, 'FIRE_YEAR'], kde=True,
                              height=5, aspect=2);
            plt.axhline(y=df_powerline['FIRE_YEAR'].value_counts().mean() / 50, color='blue',
                        label='Moyenne sur l\'ensemble des états');
            plt.title(f'Nombre de feux par an pour {selected_state}', fontsize=15)
            plt.legend();
            st.pyplot(fig)

        if selected_state == Top_state[4]:
            fig = sns.displot(df_powerline.loc[df_powerline['STATE'] == selected_state, 'FIRE_YEAR'], kde=True,
                              height=5, aspect=2);
            plt.axhline(y=df_powerline['FIRE_YEAR'].value_counts().mean() / 50, color='blue',
                        label='Moyenne sur l\'ensemble des états');
            plt.title(f'Nombre de feux par an pour {selected_state}', fontsize=15)
            plt.legend();
            st.pyplot(fig)

    st.markdown('## La recette du Texas pour les feux')
    with st.expander('Un réseau exposé'):
        st.markdown(
            'Le Texas est principalement équipé de lignes aériennes du fait de son réseau ancien et du coût important'
            ' des lignes enterrées. La majorité du réseau Texan est donc très exposé aux incidents qui déclenchent'
            ' les incendies. ')
        st.markdown(
            '**Les lignes tombées au sol** – Les lignes électriques peuvent tomber au sol (pour de nombreuses raisons), '
            'les disjoncteurs devraient se déclencher, mais dans 30 % des cas, ils consomment trop peu de courant pour '
            'fonctionner correctement et la ligne peut arquer pendant une longue période avant que le courant ne soit coupé.')
        st.markdown(
            '**Les contacts avec la végétation** – Les arbres et autres végétaux qui s\'immiscent dans les lignes électriques '
            'peuvent provoquer des incendies de multiples façons, comme la chute d\'un arbre sur une ligne ou une branche qui '
            'touche deux caténaires.')
        st.markdown(
            '**Un contact entre les caténaires** – Les caténaires doivent être suffisamment espacés mais, dans certaines '
            'conditions (comme un vent fort), ils se touchent, forment des arcs et répandent des particules métalliques chaudes '
            'qui peuvent enflammer la végétation sèche alentour.')
        st.markdown(
            '**Une défaillance de l\'équipement** – De nombreux composants des lignes électriques sont conçus pour servir un '
            'certain nombre d\'années et doivent être remplacés à intervalles réguliers. Sinon, ils tombent en panne.')

    with st.expander('Le Texas a son propre réseau électrique'):
        st.markdown(
            'Le Texas est le seul État américain dont le réseau électrique n\'est pas interconnecté au reste du pays. C\'est '
            'l\'une des raisons de la panne massive de l\'hiver 2021. Ainsi, les infrastructures électriques ne sont pas contrôlées au '
            'niveau fédéral et sont gérées de manière incohérente avec le reste des États-Unis.')

    with st.expander('Des infrastructures vieillissantes'):
        st.markdown(
            'Des rapports provenant de nombreuses régions des États-Unis montrent que les compagnies d\'électricité sont '
            'poursuivies pour avoir négligé l\'infrastructure des lignes électriques, notamment au Texas où une grande partie de'
            'l\'infrastructure appartient à des sociétés privées. De par leur conception, elles doivent donner un retour sur '
            'investissement, et non pas fonctionner au profit du plus grand nombre en opposition avec l\'État. Le résultat est '
            'qu\'elles font le minimum pour éviter une défaillance systémique, la plupart du temps c\'est suffisant, mais en cas '
            'de conditions inhabituelles, cela conduit à des événements catastrophiques : comme en 2011.')

    with st.expander('2011'):
        st.markdown(
            '2011 est une année de La Niña, un phénomène météorologique connu pour provoquer la sécheresse au Texas. Cette '
            'condition météorologique entraîne l\'une des pires sécheresses de l\'histoire de l\'État. '
            'Voici une petite analyse des données de la NOAA :')

        # import data
        df_drougth = pd.read_csv('asset/4101-pdsi-all-4-1992-2015.csv')
        # conerting to date
        df_drougth['Month'] = df_drougth['Date'].astype('str').apply(lambda x: x[-2:])
        df_drougth['Year'] = df_drougth['Date'].astype('str').apply(lambda x: x[0:4])
        df_drougth['Day'] = '01'
        df_drougth['Date'] = pd.to_datetime(df_drougth[['Month', 'Year', 'Day']])
        df_drougth.drop(['Month', 'Year', 'Day'], inplace=True, axis=1)  # cleaning
        # seting-up the hue value
        df_drougth['anomaly symbol'] = 1
        df_drougth.loc[df_drougth['Value'] < 0, 'anomaly symbol'] = -1
        df_drougth['x_label'] = df_drougth['Date'].dt.year  # seting up the plot
        fig = plt.figure(figsize=(20, 6))
        ax = fig.add_subplot(111)
        sns.barplot(x='x_label', y='Value', hue='anomaly symbol', data=df_drougth, ax=ax);
        plt.xticks(rotation=45)
        plt.xlabel("Année")
        plt.ylabel('Index de sévérité de Palmer. 0 = Normal')
        plt.title("Évolution de l'index de sévérité de Palmer", fontsize=20)
        ax.legend_.remove();
        st.pyplot(fig)

        st.markdown('On voit ici très bien la sécheresse qui a été classée comme la pire des 127 dernières années.')

    st.markdown('## Conclusion')
    st.markdown(
        'On peut ici laisser de côté un problème dans l\'enregistrement des données, car en dehors de la période '
        'de sécheresse l\'anomalie disparaît. ')
    st.markdown('Ce qui nous laisse une conjonction de facteurs pouvant expliquer l\'anomalie :')
    st.markdown(
        '''
            - Des standards de gestion du réseau électrique très différents du reste de l\'Union,
            - Une sècheresse parmi les plus dures jamais enregistrée,
            - Des equipments vieillissants maintenant dans les conditions tout juste satisfaisante pour la continuité de l\'activité dans les conditions d\'opération normales.
        '''
        )
    st.markdown('On peut craindre que les phénomènes exceptionnels se multipliant, ce type d\'anomalie sera amené à '
                'se reproduire.')

if selected == "Et la sécheresse ?":
        
    st.markdown("## La sécheresse, facteur de risque : mythe ou réalité ?")
    tab1, tab2, tab3 = st.tabs(["🌎 US Drought Monitor", "🥵 % du territoire en sécheresse", "📊 L'indice PDSI"])

    with tab1:
        
        st.markdown("### Présentation des nouvelles données")
        
        st.markdown('**L’US Drought Monitor** est une carte publiée tous les jeudis qui montre les territoires des Etats-Unis en sécheresse :')
        image = Image.open('asset/US_Drought_Map.JPG')
        st.image(image)
        
        st.markdown('Cette carte utilise 5 classifications pour qualifier le niveau de sécheresse :')
        image = Image.open('asset/US_Drought_Ind.JPG')
        st.image(image)
        
        st.markdown('Le site https://droughtmonitor.unl.edu/ met également à disposition des séries temporelles permettant de retracer les évolutions de ces indicateurs de sécheresse à partir de 2000.')
    
        st.markdown(
            '''
                Pour les besoins de l'étude, nous allons collecter les données de l\'état du Texas sur la période 2000-2015.  
                Ci-dessous un extrait des données pour l\'été 2013 :
            '''
            )
    
        dr = pd.read_csv('asset/drought_TX.csv', sep = ',')
        dr.MapDate = pd.to_datetime(dr.MapDate, format = '%Y%m%d')
        dr.drop(['StateAbbreviation', 'StatisticFormatID', 'ValidStart', 'ValidEnd'], axis = 1, inplace = True)
        dr = dr.set_index(['MapDate'])
        dr.sort_values(by = ['MapDate'], inplace = True)
        st.dataframe(dr.iloc[702:715,:])
            
        st.markdown('*Note : données représentant le pourcentage du territoire ayant atteint le niveau de sécheresse indiqué*')
        
    with tab2:
    
        st.markdown("### Influence de la sécheresse sur le nombre de feux")
        
        st.markdown(
            '''
                Rapprochons l\'évolution du nombre de feux avec le pourcentage du territoire texan en sécheresse.  
                Pour ce faire, nous utilisons la librairie **Statsmodel** qui permet notamment de sortir des courbes de tendance à partir de séries temporelles :
            '''
            )
        
        image = Image.open('asset/US_Drought_Trend.png')
        st.image(image)
            
        st.markdown('La superposition des 2 courbes laisse à penser qu\'il y a bien un lien de corrélation entre le pourcentage du territoire texan en sécheresse (courbe bleue) et le nombre de nombre de feux recensés (courbe rouge), cette démonstration reste néanmoins insuffisante pour statuer sur le niveau de corrélation réel.')
        st.markdown('Affichons la matrice de corrélation :')
        
        image = Image.open('asset/US_Drought_Corr.png')
        st.image(image)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("### Conclusion")
        st.markdown(
            '''
                L\'influence du pourcentage de terres en sécheresse sur le nombre de feux recensés semble limité (0.36) et sans effet notable sur les surfaces brûlées (0.16).  
                Néanmoins il faut prendre ces résultats avec précaution car les données utilisées sont moyennées sur l’ensemble du territoire du Texas qui est le 2ème plus grand état du pays. Un affinage de l’étude au niveau de chaque comté pourrait mettre en avant des niveaux de corrélation plus importants.
            '''
            )
        
    with tab3:
    
        st.markdown("### Corrélation avec l''indice PDSI ?")
            
        st.markdown(
            '''
                Défini dans les années 60 et fondé sur un concept de bilan « Offre et demande » appliqué à l'humidité du sol, l'indice de sécheresse de Palmer ("Palmer Drought Severity Index" en anglais ou PDSI) est calculé à l’aide de relevés mensuels de température et précipitation, ainsi que d’informations sur la capacité de rétention d’eau du sol.  
                
                Rapprochons l'évolution de cet indice relevé sur le territoire Texan avec l'évolution du nombre de feux :
            '''
            )
                
        image = Image.open('asset/PDSI_hist.png')
        st.image(image)
        
        st.markdown('Affichons la matrice de corrélation :')
                   
        image = Image.open('asset/PDSI_Corr.png')
        st.image(image)
           
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("### Conclusion")    
        
        st.markdown(
            '''
                L'indice de sécheresse de Palmer présente un coefficient de corrélation modéré (-0.51) qui nous conforte dans l'idée que :  
                (1) La sécheresse contribue à la survenance et à la profilération des feux sans en être l'unique facteur,  
                (2) L'étude de ces phénomènes restent très complexe.
            '''
            )

if selected == "Prédiction de feu":
    model_clf = joblib.load('asset/alaska_model.pkl')

    st.markdown("## Prédiction de feu en Alaska à partir de la Météo du jour ")
    tab1, tab2 = st.tabs(["👀 Essayer le modèle", "🛠️ Infos de construction"])

    with tab1:
        st.markdown('#### Prédiction actuelle')
        # getting data from accuweather api
        response = requests.request("GET", f'https://api.openweathermap.org/data/3.0/onecall?lat=64.994774&lon=-150.631255&appid={api_token}&units=imperial')
        # building the dataframe
        # building the dataframe
        weather_data = pd.DataFrame([[response.json()['daily'][0]['temp']['day'],
                                      response.json()['daily'][0]['dew_point'],
                                      response.json()['daily'][0]['wind_speed'],
                                      response.json()['daily'][0]['wind_gust'],
                                      response.json()['daily'][0]['temp']['max'],
                                      response.json()['daily'][0]['temp']['min'],
                                      response.json()['daily'][0].get('rain')]],
                                    columns=['TEMP', 'DEWP', 'WDSP', 'GUST', 'MAX', 'MIN', 'PRCP'])
        if weather_data['PRCP'][0] == None:
            weather_data['PRCP'][0] = 0

        # prediction from data
        prediction = model_clf.predict_proba(weather_data)

        # Displaying probability
        pas_feu, feu = st.columns(2)
        pas_feu.metric("Probabilité d'avoir aucun feu", f'{round(prediction[0][0]*100, 2)} % ±15', "🌳", delta_color='off')
        feu.metric("Probabilité d'avoir un feu", f'{round(prediction[0][1]*100, 2)} % ±15', "🔥", delta_color='off')

        # Displaying the source data
        st.markdown('Cette prédiction est donnée par rapport aux prédictions météos actuelles pour la journée de demain '
                    'par openweather pour l\'Alaska')
        temperature = round(((response.json()['daily'][0]['temp']['day']) -32) / 1.8, 2)
        temperature_max = round(((response.json()['daily'][0]['temp']['max']) - 32) / 1.8, 2)
        temperature_min = round(((response.json()['daily'][0]['temp']['min']) - 32) / 1.8, 2)
        dew_point = round(((response.json()['daily'][0]['dew_point']) - 32) / 1.8, 2)
        wind_speed = round((response.json()['daily'][0]['wind_speed'])*1.6093439999999, 2)
        gust_speed = round((response.json()['daily'][0]['wind_gust'])*1.6093439999999, 2)
        precipitation = round(weather_data['PRCP'][0]*25.4, 2)

        temp, maxi, mini, dwpt, wind, gust, precip = st.columns(7)
        temp.metric('Temperature', f'{temperature}°C')
        maxi.metric('Temperature max', f'{temperature_max}°C')
        mini.metric('Temperature min', f'{temperature_min}°C')
        dwpt.metric('Point de rosé', f'{dew_point}°C')
        wind.metric('Vitesse du vent (km/h)', f'{wind_speed}')
        gust.metric('Rafales de vent (km/h)', f'{gust_speed}')
        precip.metric('Précipitations', f'{precipitation} mm')

        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown('#### Testez vos propres données')
        col1, col2 = st.columns(2)
        with col1:
            temperature_s = st.slider('Température moyenne (°C)', value=temperature, min_value=-20.0, max_value=50.0, step=1.0)*1.8+32
            temperature_max_s = st.slider('Température max (°C)', value=temperature_max, min_value=temperature_s, max_value=55.0, step=1.0)*1.8+32
            temperature_min_s = st.slider('Température min (°C)', value=temperature_min, min_value=-25.0, max_value=temperature_s, step=1.0)*1.8+32
            dew_point_s = st.slider('Point de rosée (°C)', value=dew_point, min_value=0.0, max_value=35.0, step=1.0)*1.8+32
        with col2:
            wind_speed_s = st.slider('Vitesse du vent (km/h)', value=wind_speed, min_value=0.0, max_value=100.0, step=1.0)*0.62137119223738
            gust_speed_s = st.slider('Vitesse des rafales (km/h)', value=gust_speed, min_value=wind_speed, max_value=100.0, step=1.0)*0.62137119223738
            precipitation_s = st.slider('Précipitation (mm)', value=float(precipitation), min_value=0.0, max_value=100.0, step=1.0)*0.039370078740158

        weather_data_s = pd.DataFrame([[temperature_s,
                                      dew_point_s,
                                      wind_speed_s,
                                      gust_speed_s,
                                      temperature_min_s,
                                      temperature_max_s,
                                      precipitation_s]],
                                    columns=['TEMP', 'DEWP', 'WDSP', 'GUST', 'MAX', 'MIN', 'PRCP'])

        # prediction from data
        prediction_s = model_clf.predict_proba(weather_data_s)

        # Displaying probability
        pas_feu, feu = st.columns(2)
        pas_feu.metric("Probabilité d'avoir aucun feu", f'{round(prediction_s[0][0]*100, 2)} % ±15', "🌳", delta_color='off')
        feu.metric("Probabilité d'avoir un feu", f'{round(prediction_s[0][1]*100, 2)} % ±15', "🔥", delta_color='off')

    with tab2:
        st.markdown('Ce model à été construit sur les données issues du global daily summary de la NOAA. Il regroupe '
                    'les données de millers de stations météo à la surface du globe. Après un filtrage des données sur '
                    'la période et les stations qui nous intéressent, celles-ci on été groupées par date et par état. À '
                    'chaque jour a été associé ou non la présence d\'un feu.')
        st.markdown('Un modèle d\'HistGradientBoostingClassifier qui donnait les meilleurs résultats a été entrainé '
                    'pour chaque état afin de respecter les différents biomes.')

        st.markdown('Le modèle donne d\'assez bons résultats de prédiction, en voici sa courbe ROC :')
        image = Image.open('asset/roc-curve.png')
        st.image(image)

        st.markdown('Voici la classification des features par importance dans le modèle :')
        image = Image.open('asset/feature-importance.png')
        st.image(image)

        st.markdown('L\'importance donnée à la température max nous donne un bon ordre d\'idée de l\'impact de '
                    'vagues de chaleurs exceptionnelles sur les feux.')

if selected == "Conclusion":
    
    st.markdown("<h2 style='text-align: center;'>Les mots de la fin sous forme de 🔥 Flamme 🔥</h2>", unsafe_allow_html=True)

    image = Image.open('asset/WordCloud.png')
    col1, col2, col3 = st.columns([1, 1.8, 1])
    col2.image(image, use_column_width=True)

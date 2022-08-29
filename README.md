# stage_ATB_biofilm


## Analyse qnr


2 types de scripts sont à disposition pour l'analyse de l'abondance des gènes *qnr* :
- **script_qnr_results** : fichier rmd (Rmarkdown) permettant de générer un rapport avec les principaux résultats statistiques 
- **script_qnr_plot** : fichier permettant de générer les graphes finaux

Dans chacun de ces fichiers, une fonction d'importation des tableaux Excel obtenus en sortie de CFX-Manager, ainsi qu'une fonction de tri des données de qPCR (données non quantifiables, non détectables,  ...) sont d'abord exécutées. Le fichier **explication_script_R.pptx** résume les différentes étapes et paramètres à disposition pour la fonction de tri des données (le chemin de gauche est l'exécution de base de la fonction, les paramètres "gamme" et "NTC" permettent de gérer les cas particuliers lorsqu'ils sont passés en **TRUE**).  

<br>


## Analyse *gyrA/parC*


La détection de variants au niveau des gènes *gyrA* et *parC* nécessite l'utilisation d'un cluster. Pour cela, il suffit de lancer **MobaXterm**, puis de se connecter aux serveurs GenoToul en créant une nouvelle session en ssh, en rentrant ensuite l'hôte **genologin.toulouse.inra.fr** (remote host) et enfin son identifiant GenoToul.  
Une fois connecté à son espace personnel, il suffit de se placer dans le dossier work/, et de lancer le fichier Snakefile d'éxucution du workflow en l'envoyant sur le cluster ("**sbatch commands_to_run.sh**" dans le terminal).  
<br>  
Si l'on souhaite modifier les échantillons sur lesquels travailler, il suffit de modifier les deux premières lignes du fichier Snakefile (**samples=""** et **gene=""** avec un espace entre chaque valeur). Il est également possible de modifier la base de données de référence pour le tri des données (db_ref="") et la séquence de référence servant à aligner les reads pour détecter les mutations (seq_ref="").  
Les donnés doivent cependant toujours se trouver sous la forme "**gène_numéchantillon_R1_val_1.fq**" pour le read 1 ou "**gène_numéchantillon_R2_val_2.fq**" pour le read 2 (il suffit de les renommer si ce n'est pas le cas lorsqu'on les récupère).  

Certains chemins utilisés pour récupérer les fichiers en input sont des chemins absolus. Il faudra donc modifier ces chemins si les fichiers utilisés ne sont pas dans les mêmes dossiers que ceux spécifiés dans ce script (pas de dossier spécial "data" ou "db" par exemple).  
  
<br>

Les fichiers **pourcentage_mutation_codon_gyrA/parC....py** permettent de calculer l'abondance de mutations pour chacun des échantillons étudiés. Cependant, il repose sur la **position de la mutation étudiée**. Pour *gyrA/parC* celle-ci se trouvent entre les aa 80 à 87 de la référence. Pour étudier une mutation différente, présente à une position différente d'une séquence de référence, il faudra donc changer le paramètre correspondant à la position de la mutation (**i==32** ou **i==36** pour *gyrA* par exemple)

<br>


## Analyse 16S


- Le dossier **STD** concerne le traitement des données de standards, incorporés aux échantillons pour faciliter la sélection des paramètres les plus adaptés à nos données dans le workflow d'analyse des données.

Il contient tout d'abord un fichier Rmd permettant la comparaison des différents paramètres disponibles dans le workflow d'analyse utilisé. Le dossier **data** contient les différents fichiers obtenus à la sortie du worflow sur Galaxy. Les autres fichiers et dossiers sont des fichiers intermédiaires permettant d'obtenir les figures finales.

<br>

- Le dossier **ABR_16S** contient les fichiers permettant l'analyse complète des données de séquençage de l'*ARNr16S* (diversités $\alpha$ et $\beta$, abondance différentielle, ...).

Les données de séquençage utilisées pour cette analyse sont contenues dans le dossier **data_asCount**. Le script .Rmd d'analyse de données utilise, en plus de ces fichiers, le fichier de métadonnées **metadata_16S_qnr.csv** contenant toutes les informations sur les échantillons (campagne, jour de prélèvement, matériel du coupon, ...), et le fichier **d1_FROGS_Affiliation_postprocess_abundance_biom.biom1**, fichier BIOM issu de l'analyse bioinformatique réalisée avec le pipeline FROGS sur Galaxy.









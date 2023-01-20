# SKYSPARK  

# Procédure de connexion  
##  Générer un token  

Pour générer un token, il faut utiliser la fonction "**getToken**" qui se trouve dans le fichier "**/spyspark_utils/utils.py**".  
Ce token va nous permettre d'utiliser l'API de Skyspark pour pouvoir faire diverses requêtes telles que **read** et **hisRead**.  
La fonction **getToken** contient 3 paramètres:  
-   URL  
-   Username  
-   Password  

Voici un exemple:  

>import spyspark_utils.utils as utils  
token = utils.getToken(  
     url = "URL SKYSPARK",  
     username = "username",  
     password = "password"  
)  

Une fois le Token généré, nous pouvons faire des requêtes pour obtenir les données souhaitées.


# Procédure de requêtes
Pour pouvoir faire des requêtes (read et hisRead), nous allons utiliser les fonctions qui se trouvent dans le fichier "**/spyspark_utils/api.py**"  

# Read
Exemple dans Skyspark:  
-   Par filtre:    "*readAll(site)*"  
-   Par id:        "*readAll(id==@p:<projectName>:r:<deviceID>)*" ou "*readAll(id==@<deviceID>)*"  

En fonction de la recherche qu'on veut faire, soit par id soit par filtre, on a 2 fonctions (qu'on verra dans la suite),  
et ces 2 fonctions ont quelques paramètres en commun:
|Paramètres |Description                                        |Requis|
|-----------|---------------------------------------------------|------|
|url        |lien de Skyspark                                   |X     |
|token      |Token généré auparavant                            |X     |
|project    |Nom du projet                                      |X     |

Pour faire une requête read via un **filtre**, il faut utiliser la fonction "**readByFilter**",  
En plus des paramètres cités juste au dessus, il y a aussi:

|Paramètres |Description                                        |Requis|
|-----------|---------------------------------------------------|------|
|filter     |Le(s) filtre(s) comme dans Skyspark                |X     |
|limit      |Un entier pour limiter le nombre de données reçues |      |
|contentType|Type de message demandé, "text/zinc" par défaut    |      |  

>import spyspark_utils.api as api  
readbyfilter = api.readByFilter(  
    url         =   "URL SKYSPARK",  
    token       =   "token",  
    project     =   "projectName",  
    filter      =   "point and gas",  
    limit       =   5,  
    contentType =   "application/json"  
)  

Pour faire une requête read via l'**id**, il faut utiliser la fonction "**readByID**",  
En plus des paramètres cités juste au dessus, il y a aussi:

|Paramètres |Description                                       |Requis|
|-----------|--------------------------------------------------|------|
|id         |id d'un point                                     |X     |
|contentType|Type de message demandé, "text/zinc" par défaut   |      |  

>import spyspark_utils.api as api  
readByID = api.readByID(  
    url         =   "URL SKYSPARK",  
    token       =   "token",  
    project     =   "projectName",  
    id          =   "@2616102f-2616102f",  
    contentType =   "application/json"  
)   

# hisRead
La fonction qui permet d'aller chercher l'historique de données d'un point est "**hisRead**".  
Cette fonction comprend les paramètres suivants:  

|Paramètres |Description                                        |Requis|
|-----------|---------------------------------------------------|------|
|url        |lien de Skyspark                                   |X     |
|token      |Token généré auparavant                            |X     |
|project    |Nom du projet                                      |X     |
|id         |id d'un point                                      |X     |
|range      |la date (comme dans Skyspark)                      |X     |
|contentType|Type de message demandé, "text/zinc" par défaut    |      |  

> import spyspark_utils.api as api  
hisread = api.hisRead(  
    url         =   "URL SKYSPARK",  
    token       =   "token",  
    project     =   "projectName",  
    id          =   "@2616102f-2616102f",  
    range       =   "2021-06-20, 2022-06-29",  
    contentType =   "application/json"  
)


### Content-Type

|Type   |Accept                                  |Comment                                    |
|-------|----------------------------------------|-------------------------------------------|
|Zinc   |text/zinc                               |or unspecified                             |
|Json   |application/json                        |or application/vnd.haystack+json;version=4 |
|JSON v3|application/vnd.haystack+json;version=3 |-                                          |
|Trio   |text/trio                               |-                                          |
|CSV    |text/csv                                |-                                          |
|Turtle |text/turtle                             |-                                          |
|JSON-LD|application/ld+json                     |-                                          |  

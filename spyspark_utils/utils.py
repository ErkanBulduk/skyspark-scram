from io import StringIO
import numpy as np
import pandas as pd
import spyspark_utils.scram as scram
import json
import hszinc

def getToken(url, username, password):
    token = scram.final_message(url, username, password)
    token = token["authToken"]
    return token

def checkContentType(contentType):
    """
    contentType (Content Negotiation):
        The default for all HTTP API operations is to return the result as a grid (or grids) with the MIME type "text/zinc" formatted using Zinc.
        • Zinc      text/zinc, */*, or unspecified
        • Json      application/json, or application/vnd.haystack+json;version=4
        • JSON v3   application/vnd.haystack+json;version=3
        • Trio      text/trio
        • CSV       text/csv
        • Turtle    text/turtle
        • JSON-LD   application/ld+json
    """
    if contentType in ["application/json", "table"]: return "application/json"
    # elif contentType=="text/csv": return contentType
    else: return contentType
    
def datetime_toZinc(rng):
    """Converter datetime to zinc for range"""
    if isinstance(rng, slice):
        str_rng = ",".join([hszinc.dump_scalar(p) for p in (rng.start, rng.stop)])
    elif not isinstance(rng, str):
        str_rng = hszinc.dump_scalar(rng)
    else:
        str_rng = hszinc.dump_scalar(rng, mode=hszinc.MODE_ZINC)
    return str_rng

def jsonToPandas(content):
    dico = json.loads(content)
    lignes = []
    colonnes = [list(x.values())[0] for x in dico.get("cols")]
    for x in dico.get("rows"):
        dico_row = {x: "" for x in colonnes}
        for y, z in x.items():
            if type(z) == dict and z.get("_kind") == "marker":
                dico_row[y] = "X"
            elif type(z) == dict:
                dico_row[y] = z.get("dis") or z.get("val")
            else:
                dico_row[y] = z
        ligne = []
        for i in dico_row.values():
            ligne.append(i)
        lignes.append(ligne)
    df2 = pd.DataFrame(
        np.array(lignes),
        columns=colonnes
    )
    return df2

def csvToPandas(content):
    csvStringIO = StringIO(str(content,'utf-8'))
    df = pd.read_csv(csvStringIO, sep=",")
    return df
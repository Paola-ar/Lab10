from database.DB_connect import DBConnect
from model.tratta import Tratta


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    # def __init__(self, database):
    #     self._listaSpedizioni = []

    @staticmethod
    def readAllSpedizioni(valore_inserito):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(""" SELECT LEAST(s.id_hub_origine, s.id_hub_destinazione) AS hub1,
                                  GREATEST(s.id_hub_origine, s.id_hub_destinazione) AS hub2,
                                  COUNT(*) AS numero_spedizioni,
                                  SUM(s.valore_merce) AS valore_totale
                           FROM spedizione s
                           GROUP BY hub1, hub2
                           HAVING valore_totale >= %s;""",(valore_inserito, ))
        for row in cursor:
            tratta = Tratta(row["hub1"], row["hub2"], row["numero_spedizioni"], row["valore_totale"])
            result.append(tratta)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getHubsNameState():
        conn = DBConnect.get_connection()
        hubs_dict = {}
        cursor = conn.cursor(dictionary=True)
        cursor.execute(" SELECT id,nome,stato FROM hub")

        for row in cursor:
            hubs_dict[row["id"]] = {"nome":row["nome"], "stato":row["stato"]}

        cursor.close()
        conn.close()
        return hubs_dict







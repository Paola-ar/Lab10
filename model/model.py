from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.hub_nomi = DAO.getHubsNameState()
        tratte = DAO.readAllSpedizioni(threshold)

        for hub_id in self.hub_nomi.keys():
            self.G.add_node(hub_id)


        for t in tratte:
            # guadagno medio
            if t.numero_spedizioni > 0:
                peso = t.valore_totale / t.numero_spedizioni

                if peso >= threshold:
                    # aggiungo arco pesato
                    self.G.add_edge(t.id_hub1, t.id_hub2, weight=peso)


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        risultati = []
        nomi = DAO.getHubsNameState()
        # itera su tutti gli archi del grafo, chiedendo i dati associati all'arco
        for u,v,data in self.G.edges(data=True):
            # estraggo il peso dall'attributo 'weight'
            peso = data["weight"]

            # nomi e stati dal dizionario
            nome_u = nomi.get(u, {"nome":f"Hub{u}","stato":""})
            nome_v = nomi.get(v, {"nome":f"Hub{v}","stato":""})

            if nome_u['stato'] != "" and nome_u['stato'] is not None:
                nomecompleto_u = nome_u['nome'] + " (" + nome_u['stato'] + ")"
            else:
                nomecompleto_u = nome_u['nome']

            if nome_v['stato'] != "" and nome_v['stato'] is not None:
                nomecompleto_v = nome_v['nome'] + " (" + nome_v['stato'] + ")"
            else:
                nomecompleto_v = nome_v['nome']

            tupla_arco = (u,v, nomecompleto_u, nomecompleto_v, peso)
            risultati.append(tupla_arco)
        return risultati



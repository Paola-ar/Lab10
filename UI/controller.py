import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO

        valore = self._view.guadagno_medio_minimo.value

        if valore == "":
            self._view.show_alert("Inserire un valore valido")
            return

        try:
            threshold = float(valore)
        except ValueError:
            self._view.show_alert("Il valore del guadagno minimo deve essere un numero!")
            return

        self._model.costruisci_grafo(threshold)

        num_nodes = self._model.get_num_nodes()
        num_edges = self._model.get_num_edges()
        edges = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()

        if len(edges) == 0:
            self._view.lista_visualizzazione.controls.append(ft.Text(f" Nessuna tratta supera il valore indicato.", size = 20))
        else:
            self._view.lista_visualizzazione.controls.append(ft.Text(f" Numero di Hubs : {num_nodes}"))
            self._view.lista_visualizzazione.controls.append(ft.Text(f" Numero di Tratte : {num_edges}"))
            for i,(u,v,nome_u,nome_v,peso) in enumerate(edges,1):
                self._view.lista_visualizzazione.controls.append(ft.Text(f" {i}) [{nome_u} --  {nome_v}] | guadagno medio per spedizione: {peso:.2f} €"))

        self._view.update()
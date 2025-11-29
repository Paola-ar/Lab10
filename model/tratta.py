from dataclasses import dataclass

@dataclass
class Tratta:
    id_hub1: int
    id_hub2: int
    numero_spedizioni: int
    valore_totale: int


    # def __eq__(self, other):
    #     return isinstance(other, Hub) and self.id == other.id

    def __repr__(self):
        return f"ID hub 1: {self.id_hub1}, ID hub 2:{self.id_hub2} -> num_spedizioni: {self.numero_spedizioni} per un valore totale di: {self.valore_totale}"

    def __str__(self):
        return f"{self.id_hub1} {self.id_hub2} {self.numero_spedizioni} {self.valore_totale}"

    def __hash__(self):
        return hash((self.id_hub1, self.id_hub2, self.numero_spedizioni, self.valore_totale))

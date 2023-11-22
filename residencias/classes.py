class Residencia:
    def __init__(
        self,
        num_quartos: int, 
        area: float, endereco: str, 
        alugado_em: str
    ) -> None:
        self.num_quartos = num_quartos
        self.area = area
        self.endereco = endereco
        self.alugado_em = alugado_em

    def __repr__(self):
        return (
            f"Localizado em {self.endereco} \n"
            f"Possui de área {self.area} \n"
            f"Tem {self.num_quartos} quartos"
        ) 
        
class Apartamento(Residencia):
    def __init__(self,
        num_quartos: int, 
        area: float, 
        endereco: str, 
        alugado_em: str,
        andar:int
    ) -> None:
        super().__init__(num_quartos, area, endereco, alugado_em)
        self.andar = andar 

    def __repr__(self):
        representacao = super().__repr__()
        return ( 
            f"Apartamento: \n{representacao} \n"
            f"Fica no andar {self.andar}"
        )
       
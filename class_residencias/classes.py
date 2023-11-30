from datetime import date

class Residencia:
    def __init__(
        self,
        num_quartos: int, 
        area: float, 
        endereco: str, 
    ) -> None:
        self.num_quartos = num_quartos
        self.area = area
        self.endereco = endereco
        self.alugado_em = None

    def __repr__(self):
        return (
            f"Localizado em {self.endereco} \n"
            f"Possui de área {self.area} \n"
            f"Tem {self.num_quartos} quartos"
        ) 
    
    def alugar(self):
        self.alugado_em = date.today()
        return "Imóvel alugado!"
        
class Apartamento(Residencia):
    def __init__(self,
        num_quartos: int, 
        area: float, 
        endereco: str, 
        andar:int
    ) -> None:
        super().__init__(num_quartos, area, endereco)
        self.andar = andar 

    def __repr__(self):
        representacao = super().__repr__()
        return ( 
            f"Apartamento: \n{representacao} \n"
            f"Fica no andar {self.andar}"
        )
       
class Casa(Residencia):
    def __init__(self, 
        num_quartos: int, 
        area: float, 
        endereco: str,  
        tem_garagem: bool
    ) -> None:
        super().__init__(num_quartos, area, endereco)
        self.tem_garagem = tem_garagem

    def __repr__(self):
        representacao = super().__repr__()
        return ( 
            f"Apartamento: \n{representacao} \n"
            f"Alugada no dia {self.alugado_em}"
        )

    
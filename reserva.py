from professor import Professor
from sala import Sala

class Reserva:

    def __init__(self, sala: Sala, professor: Professor, data_hora, obs) -> None:
        if not isinstance(sala, sala):
            pass
        if not isinstance(professor, professor):
            pass

        self.__professor = professor
        self.__sala = sala
        self.__data_hora = data_hora
        self.__observacao = obs
    
    @property
    def professor(self):
        return self.__professor
    
    @property
    def sala(self):
        return self.__sala
    
    @property
    def data_hora(self):
        return self.__data_hora
    
    @data_hora.setter
    def data_hora(self, data_hora):
        self.__data_hora = data_hora  
    
    @property
    def observacao(self):
        return self.__observacao
    
    @observacao.setter
    def observacao(self, obs):
        self.__observacao = obs  

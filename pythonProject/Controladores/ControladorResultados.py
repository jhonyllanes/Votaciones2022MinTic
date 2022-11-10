from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Modelos.Resultados import Resultados
from Repositorios.RepositorioMesas import RepositorioMesas
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioResultados import RepositorioResultados
class ControladorResultados():
    def __init__(self):
        self.repositorioMesas = RepositorioMesas()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioResultados = RepositorioResultados()
    def index(self):
        return self.repositorioResultados.findAll()
    """
     Asignacion mesa y candidato a resultado
    """
    def create(self,infoResultados,id_mesa,id_candidato):
        nuevoResultado=Resultados(infoResultados)
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa=Mesa(self.repositorioMesas.findById(id_mesa))
        nuevoResultado.candidato=elCandidato
        nuevoResultado.mesa=laMesa
        return self.repositorioResultados.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__

    def update(self,id,infoResultados,id_mesa,id_candidato):
        elResultado=Resultados(self.repositorioResultados.findById(id))
        elResultado.cantidad_votos=infoResultados["cantidad votos"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultados.save(elResultado)

    def listarInscritosEnMesa(self, id_mesa):
        return self.repositorioResultados.getListadoResultadosEnMesa(id_mesa)


    


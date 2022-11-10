from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados

from bson import ObjectId

class RepositorioResultados(InterfaceRepositorio[Resultados]):
    class RepositorioResultado(InterfaceRepositorio[Resultados]):

        def getListadoResultadosEnMesa(self, id_mesa):
            theQuery = {"mesa.$id": ObjectId(id_mesa)}
            return self.query(theQuery)


        def getMayorVotosPorMesa(self):
            query1 = {
                "$group": {
                    "_id": "mesa",
                    "max": {
                        "$max": "$numero de votos"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
            pipeline = [query1]
            return self.queryAggregation(pipeline)
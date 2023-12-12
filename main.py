from experta import *


class CarreraFact(Fact):
    pass


class CarreraRules(KnowledgeEngine):
    @Rule(
        OR(
            AND(CarreraFact(pregunta='actividad', respuesta='a')),
            AND(CarreraFact(pregunta='tiempo_libre', respuesta='a')),
            AND(CarreraFact(pregunta='habilidades', respuesta='a')),
            AND(CarreraFact(pregunta='proyectos', respuesta='a')),
            AND(CarreraFact(pregunta='trabajo_equipo', respuesta='a'))
        )
    )
    def carrera_finanzas(self):
        self.declare(Fact(carrera='Finanzas o Contaduría Pública'))

    @Rule(
        OR(
            AND(CarreraFact(pregunta='actividad', respuesta='b')),
            AND(CarreraFact(pregunta='tiempo_libre', respuesta='b')),
            AND(CarreraFact(pregunta='habilidades', respuesta='b')),
            AND(CarreraFact(pregunta='proyectos', respuesta='b')),
            AND(CarreraFact(pregunta='trabajo_equipo', respuesta='b'))
        )
    )
    def carrera_administracion(self):
        self.declare(Fact(carrera='Administración de Empresas o Ingeniería Industrial'))

    @Rule(
        OR(
            AND(CarreraFact(pregunta='actividad', respuesta='c')),
            AND(CarreraFact(pregunta='tiempo_libre', respuesta='c')),
            AND(CarreraFact(pregunta='habilidades', respuesta='c')),
            AND(CarreraFact(pregunta='proyectos', respuesta='c')),
            AND(CarreraFact(pregunta='trabajo_equipo', respuesta='c'))
        )
    )
    def carrera_geologia(self):
        self.declare(Fact(carrera='Ingeniería de Minas o Geología'))

    @Rule(
        OR(
            AND(CarreraFact(pregunta='actividad', respuesta='d')),
            AND(CarreraFact(pregunta='tiempo_libre', respuesta='d')),
            AND(CarreraFact(pregunta='habilidades', respuesta='d')),
            AND(CarreraFact(pregunta='proyectos', respuesta='d')),
            AND(CarreraFact(pregunta='trabajo_equipo', respuesta='d'))
        )
    )
    def carrera_electronica(self):
        self.declare(Fact(carrera='Ingeniería Electrónica o Ingeniería de Sistemas y Computación'))

    @Rule(
        OR(
            AND(CarreraFact(pregunta='actividad', respuesta='e')),
            AND(CarreraFact(pregunta='tiempo_libre', respuesta='e')),
            AND(CarreraFact(pregunta='habilidades', respuesta='e')),
            AND(CarreraFact(pregunta='proyectos', respuesta='e')),
            AND(CarreraFact(pregunta='trabajo_equipo', respuesta='e'))
        )
    )
    def carrera_comercio(self):
        self.declare(Fact(carrera='Comercio Internacional'))


if __name__ == "__main__":
    engine = CarreraRules()

    preguntas = ['actividad', 'tiempo_libre', 'habilidades', 'proyectos', 'trabajo_equipo']

    for pregunta in preguntas:
        respuesta = input(f"¿Cómo responderías a la pregunta sobre {pregunta}? (a, b, c, d, e): ").lower()
        engine.declare(CarreraFact(pregunta=pregunta, respuesta=respuesta))

    engine.run()

    # Accede al hecho 'carrera' directamente desde la base de hechos
    carrera_fact = engine.facts.find(lambda fact: isinstance(fact, Fact) and 'carrera' in fact.fields)

    if carrera_fact:
        print("\n¡Tu sugerencia de carrera es:", carrera_fact['carrera'], "!")
    else:
        print("\n¡No se pudo determinar una sugerencia de carrera!")
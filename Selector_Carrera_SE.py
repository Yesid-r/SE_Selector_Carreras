from experta import Fact, KnowledgeEngine, DefFacts, Rule, OR, NOT, MATCH, W

# Lista de carreras
carreras_list = []
# Características de las carreras
carreras_char = []
carreras_map = {}


def preprocess():
    global carreras_list, carreras_char, carreras_map
    # Abrir el archivo y leer los datos
    carreras_file = open("Carreras.txt")
    carreras_data = carreras_file.read()
    dcarreras_list = carreras_data.split("\n")
    carreras_file.close()
    for c in dcarreras_list:
        if c == "":
            continue
        char_file = open("Carrera_Caracteristicas/" + c + ".txt")
        char_data = char_file.read()
        char_list = char_data.split("\n")
        carreras_char.append(char_list)
        carreras_map[str(char_list)] = c
        char_file.close()


def identify_carrera(*arguments):
    # Lista de características
    char_list = []
    for char in arguments:
        char_list.append(char)
    # Manejar errores de clave
    return carreras_map[str(char_list)]


def if_not_matched(c):
    print("")
    id_c = c
    print("")
    print("La carrera recomendada para ti es: %s\n" % (id_c))


class OrientacionProfesional(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("¡Hola! Soy el asistente de orientación profesional. Estoy aquí para ayudarte a elegir la mejor carrera para ti.\n")
        print("Este sistema experto te ayudará a seleccionar la carrera más adecuada para tus intereses y habilidades.\n")
        print("Por eso, es preferible analizar tus preferencias en relación con un conjunto de preguntas siguientes:")
        print("")
        yield Fact(action="find_carrera")

    # Definición de reglas base
    @Rule(Fact(action='find_carrera'), NOT(Fact(interes_minas=W())), salience=1)
    def question_0(self):
        self.declare(Fact(interes_minas=input("¿Te interesa trabajar con recursos naturales y geología?")))

    @Rule(Fact(action='find_carrera'), NOT(Fact(interes_sistemas=W())), salience=1)
    def question_1(self):
        self.declare(Fact(interes_sistemas=input("¿Disfrutas de la programación y la tecnología informática?")))

    @Rule(Fact(action='find_carrera'), NOT(Fact(interes_administracion=W())), salience=1)
    def question_2(self):
        self.declare(Fact(interes_administracion=input("¿Te atrae la toma de decisiones estratégicas y la gestión de empresas?")))

    @Rule(Fact(action='find_carrera'), NOT(Fact(interes_industrial=W())), salience=1)
    def question_3(self):
        self.declare(Fact(interes_industrial=input("¿Prefieres trabajar en la optimización de procesos y sistemas?")))

    @Rule(Fact(action='find_carrera'), NOT(Fact(interes_minas2=W())), salience=1)
    def question_4(self):
        self.declare(Fact(interes_minas2=input("¿Te interesa la exploración y explotación de recursos minerales?")))

    @Rule(Fact(action='find_carrera'), NOT(Fact(interes_sistemas2=W())), salience=1)
    def question_5(self):
        self.declare(Fact(interes_sistemas2=input("¿Te apasiona el diseño y la implementación de software?")))

    @Rule(Fact(action='find_carrera'), NOT(Fact(interes_industrial2=W())), salience=1)
    def question_6(self):
        self.declare(Fact(interes_industrial2=input("¿Te atrae la gestión eficiente de recursos y la mejora continua en procesos?")))

    @Rule(Fact(action='find_carrera'), NOT(Fact(interes_administracion2=W())), salience=1)
    def question_7(self):
        self.declare(Fact(interes_administracion2=input("¿Te gusta planificar y supervisar proyectos desde su concepción hasta su implementación?")))

    @Rule(Fact(action='find_carrera'), Fact(interes_minas="si"), OR(Fact(interes_sistemas="no")),
          Fact(interes_administracion="no"), OR(Fact(interes_industrial="no")), OR(Fact(interes_minas2="si"),
                                                                                    Fact(interes_sistemas2="no"),
                                                                                    Fact(interes_industrial2="no"),
                                                                                    Fact(interes_administracion2="no")))
    def carrera_0(self):
        self.declare(Fact(c="Ingeniería de Minas"))
        self.declare(Fact(clrShowed="yes"))

    @Rule(Fact(action='find_carrera'), Fact(interes_minas="no"), OR(Fact(interes_sistemas="si")),
          Fact(interes_administracion="no"), OR(Fact(interes_industrial="no")), OR(Fact(interes_minas2="no"),
                                                                                    Fact(interes_sistemas2="si"),
                                                                                    Fact(interes_industrial2="no"),
                                                                                    Fact(interes_administracion2="no")))
    def carrera_1(self):
        self.declare(Fact(c="Ingeniería de Sistemas"))
        self.declare(Fact(clrShowed="yes"))

    @Rule(Fact(action='find_carrera'), Fact(interes_minas="no"), OR(Fact(interes_sistemas="no")),
          Fact(interes_administracion="si"), OR(Fact(interes_industrial="no")), OR(Fact(interes_minas2="no"),
                                                                                    Fact(interes_sistemas2="no"),
                                                                                    Fact(interes_industrial2="no"),
                                                                                    Fact(interes_administracion2="si")))
    def carrera_2(self):
        self.declare(Fact(c="Administración"))
        self.declare(Fact(clrShowed="yes"))

    @Rule(Fact(action='find_carrera'), Fact(interes_minas="no"), OR(Fact(interes_sistemas="no")),
          Fact(interes_administracion="no"), OR(Fact(interes_industrial="si")), OR(Fact(interes_minas2="no"),
                                                                                     Fact(interes_sistemas2="no"),
                                                                                     Fact(interes_industrial2="si"),
                                                                                     Fact(interes_administracion2="no")))
    def carrera_3(self):
        self.declare(Fact(c="Ingeniería Industrial"))
        self.declare(Fact(clrShowed="yes"))

    @Rule(Fact(action='find_carrera'), Fact(c=MATCH.c), salience=-998)
    def c(self, c):
        print("")
        id_c = c
        print("")
        print("La carrera recomendada para ti es: %s\n" % (id_c))

    @Rule(Fact(action='find_carrera'),
          Fact(interes_minas=MATCH.interes_minas),
          Fact(interes_sistemas=MATCH.interes_sistemas),
          Fact(interes_administracion=MATCH.interes_administracion),
          Fact(interes_industrial=MATCH.interes_industrial),
          Fact(interes_minas2=MATCH.interes_minas2),
          Fact(interes_sistemas2=MATCH.interes_sistemas2),
          Fact(interes_industrial2=MATCH.interes_industrial2),
          Fact(interes_administracion2=MATCH.interes_administracion2), NOT(Fact(c=MATCH.c)), salience=-999)
    def not_matched(self, interes_minas, interes_sistemas, interes_administracion, interes_industrial, interes_minas2,
                    interes_sistemas2, interes_industrial2, interes_administracion2):
        print("\nNo he encontrado una carrera que coincida exactamente con las características dadas.")
        char_list = [interes_minas, interes_sistemas, interes_administracion, interes_industrial, interes_minas2,
                     interes_sistemas2, interes_industrial2, interes_administracion2]

        max_count = 0
        max_carrera = ""
        for key, val in carreras_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(len(char_list)):
                if temp_list[j] == char_list[j] and char_list[j] == "si":
                    count += 1
            if count > max_count:
                max_count = count
                max_carrera = val
        if_not_matched(max_carrera)


if __name__ == "__main__":
    preprocess()
    engine = OrientacionProfesional()
    while 1:
        engine.reset()  # Prepara el motor para la ejecución.
        engine.run()  # ¡Ejecútalo!
        print("¿Quieres elegir otra carrera?")
        if input() == "no":
            exit()

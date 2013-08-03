# -*- coding: utf-8 -*-

import os
import sqlite3

def create_db(db_name):
    conn = sqlite3.connect(db_name)
    c= conn.cursor()
    
    
    query = """CREATE TABLE categorias (id_categoria integer PRIMARY KEY AUTOINCREMENT,
                                        nombre text)"""
      
    c.execute(query)
    
    
    query1 = """CREATE TABLE noticias(id_noticia integer primary key AUTOINCREMENT,
                                      titulo text,
                                      fecha date,
                                      resumen text,
                                      texto text,
                                      publicada char,
                                      fk_id_categoria integer,
                                      autor text,
			                          FOREIGN KEY (fk_id_categoria) REFERENCES categorias (id_categoria))"""
    c.execute(query1)
    
if __name__ == "__main__":
    db_name = 'base1.db'
    if not os.path.exists(db_name):
        create_db(db_name)
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()


    query = "INSERT INTO categorias (id_categoria,nombre) VALUES (?,?)"	
    
    
    c1 =["1",u"Economía"]
    c2 =["2","Deportes"]
    c3 =["3",u"Tecnología"]
    c4 =["4","Panoramas"]
    c5 =["5","Tendencias y mujer"]
    c6 =["6",u"Música"]
    c7 =["7","Mundo"]
    c8 =["8",u"Cultura y espectáculos"]
    c9 =["9",u"Educación"]
    c10 =["10","Chile"]    
    
    
    c.execute("INSERT INTO categorias VALUES (?,?)",c1)
    c.execute("INSERT INTO categorias VALUES (?,?)",c2)
    c.execute("INSERT INTO categorias VALUES (?,?)",c3)
    c.execute("INSERT INTO categorias VALUES (?,?)",c4)	
    c.execute("INSERT INTO categorias VALUES (?,?)",c5)
    c.execute("INSERT INTO categorias VALUES (?,?)",c6)
    c.execute("INSERT INTO categorias VALUES (?,?)",c7)
    c.execute("INSERT INTO categorias VALUES (?,?)",c8)
    c.execute("INSERT INTO categorias VALUES (?,?)",c9)
    c.execute("INSERT INTO categorias VALUES (?,?)",c10)
    	
    conn.commit()

	
    query1 = "INSERT INTO noticias(id_noticia,titulo,fecha,resumen,texto,publicada,fk_id_categoria,autor) VALUES (?,?,?,?,?,?,?,?)"
   
    n1=["11",u"Precios de las bencinas volverían a registrar una nueva alza la próxima semana","02-08-2013",
        u"El próximo jueves el valor de las gasolinas registrarían un aumento promedio de $8, según estimaciones de Econsult.",
        u"A los $18 que aumentó en promedio el precio de las bencinas durante esta semana, el próximo jueves el valor del combustible registraría un nuevo aumento, según estimaciones realizadas por la consultora, Econsult.",
        "Si",
        "1",
        u"Juan Pérez"]
    n2=["12","Bolsa de Santiago cae por toma de ganancias y a la espera de resultados empresariales","02-08-2013",
        u"El IPSA -que agrupa a las 40 principales acciones de la plaza bursátil local- cedió un 0,26%, a 3.820,54 puntos.",
        u"El IPSA -que agrupa a las 40 principales acciones de la plaza bursátil local- cedió un 0,26%, a 3.820,54 puntos, mientras que el indicador general IGPA descendió un 0,23%, a 18.789,28 unidades. En la semana, el IPSA acumuló un avance del 0,3%.",
        "No",
        "1",
        "Camilo Urrutia"]  
    n3=["13",u"Tenis: Chilenas Cecilia Costa y Macarena Olivares protagonizarán la final del ITF de La Paz","03-08-2013",
        u"La segunda raqueta nacional venció a la mexicana Regina Clark por 7-6 (2) 4-6 y 6-2; mientras que la cinco del país derrotó a la argentina Sofía Luini por 6-4 y 7-5. ",
        u"La tenista nacional Cecilia Costa (375°) consiguió el paso a la final del ITF de La Paz, Bolivia, al vencer este viernes a la mexicana Regina Clark (s-r) en tres sets, por 7-6 (2) 4-6 y 6-2.Fue un triunfo muy trabajado el de la raqueta número dos de Chile, lo que queda de manifiesto en el marcador final. ",
        "Si",
        "2",
        "Felipe Castro"]    
    n4=["14",u"Sebastián Sáez, goleador de los últimos dos torneos chilenos, parte a Qatar","03-08-2013",
        u"El delantero argentino que triunfara en Audax Italiano está en Medio oriente realizando los exámenes médicos para firmar en un club asiático. ",
        u"El goleador de los últimos dos torneos chilenos, Sebastián Sáez, viajó a Qatar para someterse a exámenes médicos y así poder sellar su paso a un equipo de Medio Oriente.El trasandino, que triunfara en Audax Italiano, cierra así las puertas ante los intentos de Colo Colo y Universidad de Chile que consultaron por él para reforzar sus ataques.",
        "Si",
        "2",
        "Felipe Castro"]    
    n5=["15",u"E-books: EE.UU. establece reglas más estrictas para Apple tras condena","03-08-2013",
        u"Entre sus exigencias, el Departamento de Justicia solicita que la empresa se abstenga durante cinco años de firmar nuevos acuerdos de distribución de libros electrónicos.",
        u"El Departamento de Justicia norteamericano presentó hoy una serie de propuestas que limitarán el negocio con contenidos digitales de Apple en Estados Unidos después de que la empresa perdiera el juicio por acordar precios de e-books.",
        "No",
        "3",
        "Javiera Riveros"]
    n6=["16",u"Usuario de Tumblr crea un sitio para publicar las fotos capturadas por quien robó su teléfono.","03-08-2013",
        u"Hafid, un ladrón que vive en Dubai, no desactivó la función de respaldo automático en Dropbox, por lo que cada foto y video que graba, termina en la cuenta del dueño original del equipo.",
        u"Durante unas vacaciones en Ibiza, España, un usuario de iPhone dejó su teléfono en la orilla de la playa mientras se bañaba en el mar. Cuando salió, el equipo y todas sus posesiones habían desaparecido. En el hotel le explicaron que un grupo de ladrones con lentes de visión nocturna solían instalarse en las dunas de la playa, esperando que alguien dejara sus cosas desatendidas y las robaban.",
        "Si",
        "3",
        "Javiera Riveros"]        
    n7=["17",u"Teatro","15-11-2011",
        u"Gira Teatro Mori-Movistar",
        u"Después de una exitosa temporada en Valdivia y Antofagasta, la gira de Teatro Mori Movistar tendrá como tercer destino la ciudad de Concepción. Tres obras de teatro y en total seis funciones de corrido, se presentarán en el Teatro Municipal de Antofagasta. ",
        "No",
        "4",
        "Carmen Gloria Alvarado"]        
    n8=["18",u"Cine","10-04-2012",
        u"Mi villano favorito 2",
        u"Gru es uno de los mayores supervillanos del mundo, pero ha decidido dejar atrás su carrera de maldad para convertirse en el papá perfecto. Mientras lo intenta, es reclutado por una organización anticriminal y supersecreta. ",
        "Si",
        "4",
        "Carmen Gloria Alvarado"] 
    n9=["19",u"Teresa Marinovic: La voz provocadora que dispara contra moros y cristianos.","09-10-2001",
        u"Esta filósofa, desde su tribuna, defiende ideas que cree han estado silenciadas por cobardía y frivolidad. Se define como ultraconservadora porque en el fondo es liberal y reconoce que se ha ganado enemigos entre los suyos.",
        u"Teresa Marinovic (40), hoy también columnista de LUN, se define como una mujer ultraconservadora y cuica, de la cota mil (porque rechaza denominarse de clase media como lo hacen todos los políticos) y en esa calidad resolvió levantar su voz. Le escribió al editor de El Mostrador y se ofreció de columnista; desde entonces, sólo saca ronchas con sus textos.",
        "No",
        "5",
        "Jose Riquelme"]               
    n10=["20",u"La historia de una pareja transexual que conmueve al mundo.","04-08-2013",
         u"Luego de sus respectivas operaciones de cambio de sexo, han enfrentado juntos la discriminación.",
         u"El Daily Mail ha expuesto su historia porque ha conmovido a muchos. Han debido recorrer un largo camino para poder mostrarse tal como se sienten y no como llegaron al mundo.Se trata de Arin Andrews y Katie Hill, jóvenes de 16 y 18 años, quienes se han dado mutuo apoyo en el proceso de cambio de sexo que hoy los tiene convertidos en la pareja transexual más famosa del momento. ",
         "Si",
         "5",
         "Jose Riquelme"]
    n11=["21",u"Fernando Milagros:Nunca he sido un cantautor","28-07-2013",
         u"Tras el éxito de San Sebastián (2011), el músico publica San Sebastián remix Vol.I, donde las canciones de ese disco son totalmente reinterpretadas por sus amigos de la escena electrónica.",
         u"Fue el tercer disco como solista en la trayectoria de Fernando Milagros, y el que marcó su despegue definitivo. No hubo lista de mejores álbumes de 2011 en la que San Sebastián no figurara, gracias a un set de diez canciones en las que plantó una mirada propia dentro del universo de cantautores que entonces emergía en Chile.",
         "No",
         "6",
         u"Carlos Oñate"]             
    n12=["22",u"Anuncian DVD alternativo y reiteran sospechas:Los lados B de Los Bunkers","01-08-2013",
         u"El grupo penquista cree que hay algo detrás del proceso en contra de Manuel Lagos, su manager en Santiago, hasta donde llegaron para ofrecer su mayor concierto en solitario. El evento será registrado para un DVD. ",
         u"Varias características hacen que, en las horas previas, el concierto que este viernes ofrecerán Los Bunkers en Santiago asome como un evento especial. Desde luego, será primera vez que convocan por sí solos a un recinto tan masivo como Movistar Arena; además, será su retorno a Chile desde el bullado incidente en la productora Evolución; y, finalmente, todo quedará registrado en un DVD que el grupo lanzará en los meses venideros.",
         "Si",
         "6",
         u"Carlos Oñate"]
    n13=["23",u"Presidio perpetuo a pareja que torturó y mató de hambre a su hijo de 4 años.","02-08-2013",
         u"El pequeño murió en su habitación en marzo de 2012 tras permanecer encerrado durante 33 horas en ella sin calefacción, sin comida y con una herida en la cabeza causada por sus padres.",
         u"LONDRES.- Una pareja fue condenada hoy a cadena perpetua por un tribunal británico por el brutal asesinato de su hijo de sólo cuatro años, al que pegaron y privaron de alimento hasta su muerte, en actos, según la jueza, de una crueldad inimaginable.",
         "Si",
         "7",
         u"Jaime Alarcón"]
    n14=["24",u"Embajadas británicas en Medio Oriente refuerzan su vigilancia tras alerta de ataque terrorista.","10-09-2009",
         u"A diferencia de Estados Unidos, Reino Unido mantendrá abiertas sus sedes diplomáticas, pero con un alto despliegue de sus efectivos de seguridad.",
         u"LONDRES.- Las embajadas británicas en Medio Oriente reforzaron este viernes su vigilancia como precaución tras la alerta mundial de viaje emitida por Estados Unidos ante la posibilidad de que el grupo terrorista Al Qaeda cometa ataques no especificados.",
         "Si",
         "7",
         u"Jaime Alarcón"]    
    n15=["25",u"Ellen DeGeneres presentará los premios Oscar 2014.","02-08-2013",
         u"La conocida animadora de la televisión estadounidense ya había sido presentadora de los premios de la Academia en 2007.",
         u"LOS ANGELES.- Ellen DeGeneres, todo un icono de la televisión en Estados Unidos, repetirá como presentadora en la próxima edición de los Oscar, tarea que ya cumplió en la gala de 2007, informó hoy en un comunicado la Academia de Hollywood.Estamos entusiasmados de tener a Ellen al frente de los Oscar, indicaron Craig Zadan y Neil Meron, productores de la ceremonia. ",
         "No",
         "8",
         "Eugenia Gallardo"]
    n16=["26",u"Mega termina con 23 años de Meganoticias y rebautiza sus noticiarios.","04-08-2013",
         u"Ahora Noticias ,será el nombre que a partir de mediados de agosto tendrán los informativos del canal, que hoy se encuentran en plena etapa de reestructuración.",
         u"SANTIAGO.- Fueron 23 años de un nombre que no siempre logró consolidarse en las preferencias de la audiencia, pero que al menos sí se transformó en marca registrada: Meganoticias.Sin embargo, el noticiario que tuvo Mega desde su propia salida al aire en 1990 (entonces como Megavisión) se acabará a mediados de este mes, para dar paso a una nueva apuesta informativa: Ahora Noticias.",
         "Si",
         "8",
         "Eugenia Gallardo"]
    n17=["27",u"Simce de Ed. Física: El 44% de los alumnos de 8° básico tiene obesidad o sobrepeso.","15-07-2013",
         u"El test también reveló que el 23% de los estudiantes está en riesgo de desarrollar enfermedades cardiacas y metabólicas cuando sean adultos. Las mujeres obtuvieron los resultados más preocupantes. ",
         u"SANTIAGO.- Preocupantes fueron los resultados que arrojó el último Simce de Educación Física, aplicado en noviembre pasado a 25 mil alumnos de Octavo Básico pertenecientes a 662 colegios del país. ",
         "Si",
         "9",
         "Enzo Lopez"]
    n18=["28",u"Universidad Católica aumenta ponderación de las notas del colegio en admisión 2014 .","03-03-2013",
         u"El NEM y el ranking de notas tendrán un valor de 40%, bajando el peso que se le asignaba a la PSU. El objetivo es que el acceso a esa universidad sea más inclusivo y equitativo. ",
         u"SANTIAGO.- La Pontificia Universidad Católica decidió aumentar significativamente el valor que le asigna a las notas de la enseñanza media para ingresar a ese plantel.A partir del proceso de admisión 2014, la universidad incrementará de un 30% a un 40% la ponderación del NEM (Notas de Enseñanza Media) y el ranking de notas, bajando a un 60% el peso de la Prueba de Selección Universitaria (PSU), informó La Segunda.",
         "No",
         "9",
         "Enzo Lopez"]         
    n19=["29",u"Sospechoso de asesinato de carabinero habría escapado al sur del país.","13-06-2009",
         u"El sujeto, quien huyó luego del mortal asalto ocurrido en Macul, es buscado intensamente por la policía.",
         u"SANTIAGO.- Mientras continúan los operativos policiales para detener a Marcial Antonio Berríos Díaz, de 41 años, sospechoso de participar en el asalto en el que fue asesinado el subteniente Daniel Silva Rodríguez, indicios en poder de los investigadores señalarían que se habría trasladado al sur del país.El sujeto permanece prófugo desde el jueves, cuando escapó luego del atraco a un local de una caja de compensación en Macul.",
         "Si",
         "10",
         "Antonio Zapata"]
    n20=["30",u"Incendio que afectó a iglesia en Valparaíso se desató en facultad de la PUCV donde se realizaba peña.","22-05-2007",
         u"Así lo estableció personal del Labocar en conjunto con Bomberos. No se descarta que el fuego se haya iniciado producto de una colilla o brasa que se quedó encendida, una falla eléctrica o incluso que haya sido intencional.",
         u"SANTIAGO.- Tras los peritajes que se realizaron esta mañana en el lugar del siniestro, se determinó que el incendio que destruyó la Iglesia San Francisco de Valparaíso se inició en dependencias de la Universidad Católica de Valparaíso, aledaña al templo, en el cerro Barón.",
         "No",
         "10",
         "Antonio Zapata"]
    
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n1)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n2)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n3)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n4)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n5)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n6)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n7)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n8)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n9)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n10)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n11)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n12)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n13)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n14)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n15)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n16)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n17)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n18)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n19)
    c.execute("INSERT INTO noticias VALUES (?,?,?,?,?,?,?,?)",n20)
    
    


    conn.commit()

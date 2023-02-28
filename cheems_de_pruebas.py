from alright import WhatsApp
import datetime, random, time
messenger = WhatsApp()
messenger.find_user('34648890328')



while (1):
    dia_semana = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month,
                               datetime.datetime.now().day).strftime("%a")

    random = random.randint(0, 30)

    messages = ["hola"]

    if(dia_semana == "Mon"):
        messenger.send_picture('./fotos/lunes.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/'+ str(random) + '.jpg')
        time.sleep(2)

        messenger.send_message("'Mi amo te quiere mucho pero le gusta dormir, por eso estoy aquí' - Cheems 1.1 <3")
        time.sleep(86400)

    if (dia_semana == "Tue"):
        for message in messages:
            messenger.send_message(message)
        messenger.send_picture('./fotos/martes.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(random) + '.jpg')
        time.sleep(2)


        time.sleep(82800)

    if (dia_semana == "Wed"):
        messenger.send_picture('./fotos/miercoles.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(random) + '.jpg')
        time.sleep(2)
        messenger.send_message("'Mi amo te quiere mucho pero le gusta dormir, por eso estoy aquí' - Cheems 1.1 <3")
        time.sleep(82800)

    if (dia_semana == "Thu"):
        messenger.send_picture('./fotos/jueves.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(random) + '.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/error.png')
        time.sleep(82800)

    if (dia_semana == "Fri"):
        messenger.send_picture('./fotos/viernes.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(random) + '.jpg')
        time.sleep(2)
        messenger.send_message("'Mi amo te quiere mucho pero le gusta dormir, por eso estoy aquí' - Cheems 1.1 <3")
        time.sleep(82800)

    if (dia_semana == "Sat"):
        messenger.send_picture('./fotos/sabado.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(random) + '.jpg')
        time.sleep(2)
        messenger.send_message("'Mi amo te quiere mucho pero le gusta dormir, por eso estoy aquí' - Cheems 1.1 <3")
        time.sleep(82800)

    if (dia_semana == "Sun"):
        messenger.send_picture('./fotos/domingo.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(random) + '.jpg')
        time.sleep(2)
        messenger.send_message("'Mi amo te quiere mucho pero le gusta dormir, por eso estoy aquí' - Cheems 1.1 <3")
        time.sleep(82800)
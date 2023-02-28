from alright import WhatsApp
import datetime, random, time, sys

if len(sys.argv) == 1:
    print("Error: Cheems <Nº de teléfono> (Formato = 'XXYYYYYYYYY')\n")
    sys.exit()

messenger = WhatsApp()
messenger.find_user(sys.argv[1])

while (1):
    day = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month,
                        datetime.datetime.now().day).strftime("%a")

    nrandom = random.randint(0, 30)

    if(day == "Mon" and datetime.datetime.now().hour == 7):
        messenger.send_picture('./fotos/lunes.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/'+ str(nrandom) + '.jpg')
        time.sleep(86400)

    if (day == "Tue" and datetime.datetime.now().hour == 7):
        messenger.send_picture('./fotos/martes.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(nrandom) + '.jpg')
        time.sleep(86400)

    if (day == "Wed" and datetime.datetime.now().hour == 7):
        messenger.send_picture('./fotos/miercoles.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(nrandom) + '.jpg')
        time.sleep(86400)

    if (day == "Thu" and datetime.datetime.now().hour == 7):
        messenger.send_picture('./fotos/jueves.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(nrandom) + '.jpg')
        time.sleep(86400)

    if (day == "Fri" and datetime.datetime.now().hour == 7):
        messenger.send_picture('./fotos/viernes.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(nrandom) + '.jpg')
        time.sleep(86400)

    if (day == "Sat" and datetime.datetime.now().hour == 7):
        messenger.send_picture('./fotos/sabado.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(nrandom) + '.jpg')
        time.sleep(86400)

    if (day == "Sun" and datetime.datetime.now().hour == 7):
        messenger.send_picture('./fotos/domingo.jpg')
        time.sleep(2)
        messenger.send_picture('./fotos/' + str(nrandom) + '.jpg')
        time.sleep(86400)



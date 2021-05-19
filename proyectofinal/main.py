from tkinter import *
from tkinter import ttk, messagebox
import statistics as stats

import MySQLdb
import numpy as np
import matplotlib.pyplot as plt

patronNomApe = '^([A-Z]\D+)$'
patronCp = '\d{5}$'
patronTelefono = '\d{9}$'
patronCod_Historia = '\d'
patronfecha = '^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$'


def mostrarGrafica():
    lista = obtenerDatos()
    n_data = 3
    values_1 = (lista[0], lista[1], lista[2])

    fig, ax = plt.subplots()
    index = np.arange(n_data)
    bar_width = 0.35

    rects1 = plt.bar(index, values_1, bar_width, color='r', label='Valores 1')

    plt.xlabel('Etiquetas')
    plt.ylabel('Valores')
    plt.title('Comparación Médicos, Pacientes e Ingresos')
    plt.xticks(index + bar_width, ('Pacientes', 'Ingresos', 'Medicos'))
    plt.legend

    plt.tight_layout()
    plt.show()


def media():
    miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
    lista = []
    lista2 = []

    cur = miConexion.cursor()
    cur.execute("SELECT fecha_ingreso from ingresos group by fecha_ingreso")
    for row in cur.fetchall():
        lista.append(row)

    for i in lista:
        sql = ("SELECT count(fecha_ingreso) from ingresos where fecha_ingreso = %s")
        datos = (i)
        cur.execute(sql, datos)
        for row in cur.fetchall():
            lista2.append(row)
    miConexion.close()

    lista2 = set().union(*lista2)

    medi.set(stats.mean(lista2))


def calcularPorcentaje():
    miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
    num1 = 0
    num2 = 0
    porcentj = 0
    lista1 = []
    lista2 = []
    fechporcen = fech.get()
    cur = miConexion.cursor()
    sql = ("SELECT fecha_ingreso from ingresos where fecha_ingreso = %s")
    datos = fechporcen
    cur.execute(sql, [datos])
    for row in cur.fetchall():
        lista1.append(row)

    cur.execute("SELECT fecha_ingreso from ingresos")
    for row in cur.fetchall():
        lista2.append(row)

    num2 = len(lista2)
    num1 = len(lista1)
    miConexion.close()
    porcentj = num1 * num2
    porcen.set("El porcentaje es %s" % porcentj)


def obtenerDatos():
    miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
    cur = miConexion.cursor()

    lista = []

    pacientes = cur.execute("SELECT count(codpac) FROM paciente group by codpac")
    ingresos = cur.execute("SELECT count(coding) FROM ingresos group by coding")
    medicos = cur.execute("SELECT count(codmed) FROM medicos group by codmed")

    lista.append(pacientes)
    lista.append(ingresos)
    lista.append(medicos)

    print(lista)

    miConexion.close()
    return lista


def seleccion(a):
    try:
        print("seleccionado")

        name = tabla.item(tabla.selection())
        name = name.get('values')
        codpaciente.set(name[0])
        ss.set(name[1])
        nomb.set(name[2])
        ape1.set(name[3])
        dom.set(name[4])
        pob.set(name[5])
        prov.set(name[6])
        codp.set(name[7])
        tel.set(name[8])
        numi.set(name[9])
        obs.set(name[10])
    except:
        print("sin selección")


def seleccionIngreso(a):
    try:
        name = tablaIngresos.item(tablaIngresos.selection())
        name = name.get('values')

        codingreso.set(name[0])
        proc.set(name[1])
        fech.set(name[2])
        numplan.set(name[3])
        numcam.set(name[4])
        observaci.set(name[5])
    except:
        print("sin selección")


def seleccionMedico(a):
    try:
        name = tablaMedicos.item(tablaMedicos.selection())
        name = name.get('values')
        codmed.set(name[0])
        nom.set(name[1])
        ape.set(name[2])
        esp.set(name[3])
        numcol.set(name[4])
        cargo.set(name[5])
        obser.set(name[6])
    except:
        print("sin selección")


def coincidencia(patron, parametro):
    match = re.match(patron, parametro)

    return match


def verificacion(codi, seg, nombre, apellido, cp, numhis, tele):
    correcto = True
    apellidolista = apellido.split(" ")
    if (coincidencia(patronCod_Historia, codi) is None):
        correcto = False
        messagebox.showerror("Error", "El código paciente debe ser numérico")
    if (coincidencia(patronCod_Historia, seg) is None):
        correcto = False
        messagebox.showerror("Error", "La Seguridad social debe ser numérico")
    if (coincidencia(patronNomApe, nombre) is None):
        correcto = False
        messagebox.showerror("Error", "El nombre solo debe contener letras y la primera en maysuculas")
    for i in apellidolista:
        if coincidencia(patronNomApe, i) is None:
            correcto = False
            messagebox.showerror("Error", "El apellido solo debe contener letras y la primera en maysuculas")
    if (coincidencia(patronCp, cp) is None):
        correcto = False
        messagebox.showerror("Error", "El código postal debe tener al menos 5 digitos")
    if (coincidencia(patronCod_Historia, numhis) is None):
        correcto = False
        messagebox.showerror("Error", "El historia debe ser numérico")
    if (coincidencia(patronTelefono, tele) is None):
        correcto = False
        messagebox.showerror("Error", "El telefono debe tener 9 digitos")

    return correcto


def verificacionIngreso(cd, fe, nup, nuc):
    correcto = True

    if (coincidencia(patronCod_Historia, cd) is None):
        correcto = False
        messagebox.showerror("Error", "El código ingreso debe ser numérico")
    if (coincidencia(patronfecha, fe) is None):
        correcto = False
        messagebox.showerror("Error", "el campofecha debe ser dd/mm/yyyy")
    if (coincidencia(patronCod_Historia, nup) is None):
        correcto = False
        messagebox.showerror("Error", "el campo numero de planta tiene que ser numérico")
    if (coincidencia(patronCod_Historia, nuc) is None):
        correcto = False
        messagebox.showerror("Error", "el campo numero de cama tiene que ser numérico")
    return correcto


def verificacionMedico(cm, nm, ap, nuc):
    correcto = True
    apellidolista = ap.split(" ")
    if (coincidencia(patronCod_Historia, cm) is None):
        correcto = False
        messagebox.showerror("Error", "El código de medico debe ser numérico")
    if (coincidencia(patronNomApe, nm) is None):
        correcto = False
        messagebox.showerror("Error", "el nombre tiene que ser en la primera en maysuculas y solo contener letras")
    for i in apellidolista:
        if coincidencia(patronNomApe, i) is None:
            correcto = False
            messagebox.showerror("Error", "El apellido solo debe contener letras y la primera en maysuculas")
    if (coincidencia(patronCod_Historia, nuc) is None):
        correcto = False
        messagebox.showerror("Error", "el campo número de colegiado tiene que ser numérico")
    return correcto


def limpiar():
    codpaciente.set("")
    ss.set("")
    nomb.set("")
    ape1.set("")
    dom.set("")
    pob.set("")
    prov.set("")
    codp.set("")
    tel.set("")
    numi.set("")
    obs.set("")


def limpiaringreso():
    codingreso.set("")
    proc.set("")
    fech.set("")
    numplan.set("")
    numcam.set("")
    observaci.set("")


def limpiarMedico():
    codmed.set("")
    nom.set("")
    ape.set("")
    esp.set("")
    numcol.set("")
    cargo.set("")
    obser.set("")


def mostrardatos():
    tabla.delete(*tabla.get_children())
    miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
    cur = miConexion.cursor()
    cur.execute("SELECT * FROM paciente order by codpac desc ")
    for row in cur.fetchall():
        tabla.insert("", 0, values=row)
    miConexion.close()


def mostrardatosIngresos():
    tablaIngresos.delete(*tablaIngresos.get_children())
    miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
    cur = miConexion.cursor()
    cur.execute("SELECT * FROM ingresos order by coding desc ")
    for row in cur.fetchall():
        tablaIngresos.insert("", 0, values=row)
    miConexion.close()


def mostrardatosMedicos():
    tablaMedicos.delete(*tablaMedicos.get_children())
    miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
    cur = miConexion.cursor()
    cur.execute("SELECT * FROM medicos order by codmed desc ")
    for row in cur.fetchall():
        tablaMedicos.insert("", 0, values=row)
    miConexion.close()


def insertapaciente():
    codi = codpaciente.get()
    seg = (ss.get())
    nombre = (nomb.get())
    apellido = ape1.get()
    domi = dom.get()
    poblacio = pob.get()
    provin = prov.get()
    cp = codp.get()
    tele = tel.get()
    numhis = numi.get()
    obcer = obs.get()

    if (verificacion(codi, seg, nombre, apellido, cp, numhis, tele)):
        miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
        cur = miConexion.cursor()
        sql = "INSERT INTO paciente (codpac, numseg,nombre,apellido,domicilio,provincia,poblacion,cp,telefono,numhist,observa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        datos = (codi, seg, nombre, apellido, domi, poblacio, provin, cp, tele, numhis, obcer)
        cur.execute(sql, datos)
        miConexion.commit()
        miConexion.close()
        mostrardatos()
        limpiar()


def insertarMedicos():
    cm = codmed.get()
    nm = nom.get()
    ap = ape.get()
    es = esp.get()
    nuc = numcol.get()
    car = cargo.get()
    ob = obser.get()
    if (verificacionMedico(cm, nm, ap, nuc)):
        miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
        cur = miConexion.cursor()
        sql = "INSERT INTO medicos (codmed, nombre,apellidos,especialidad,num_colegiado,cargo,observaciones) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        datos = (cm, nm, ap, es, nuc, car, ob)
        cur.execute(sql, datos)
        miConexion.commit()
        miConexion.close()
        mostrardatosMedicos()
        limpiarMedico()


def modificapaciente():
    codi = codpaciente.get()
    seg = (ss.get())
    nombre = (nomb.get())
    apellido = ape1.get()
    domi = dom.get()
    poblacio = pob.get()
    provin = prov.get()
    cp = codp.get()
    tele = tel.get()
    numhis = numi.get()
    obcer = obs.get()

    if (verificacion(codi, seg, nombre, apellido, cp, numhis, tele)):
        miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
        cur = miConexion.cursor()
        sql = "UPDATE paciente SET numseg=%s,nombre=%s,apellido=%s,domicilio=%s,provincia=%s,poblacion=%s,cp=%s,telefono=%s,numhist=%s,observa=%s WHERE codpac = %s"
        datos = (seg, nombre, apellido, domi, poblacio, provin, cp, tele, numhis, obcer, codi)
        cur.execute(sql, datos)
        miConexion.commit()
        miConexion.close()
        mostrardatos()
        limpiar()


def modificarMedicos():
    cm = codmed.get()
    nm = nom.get()
    ap = ape.get()
    es = esp.get()
    nuc = numcol.get()
    car = cargo.get()
    ob = obser.get()
    if (verificacionMedico(cm, nm, ap, nuc)):
        try:
            name = tablaMedicos.item(tablaMedicos.selection())
            name = name.get('values')
            name = str(name[0])
        except:
            print("no has seleccionado nada")
        codi = codmed.get()
        if codi == 0:
            codi = name

        miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
        cur = miConexion.cursor()
        sql = "UPDATE medicos SET nombre=%s,apellidos=%s,especialidad=%s,num_colegiado=%s,cargo=%s,observaciones=%s WHERE codmed = %s"
        datos = (nm, ap, es, nuc, car, ob, cm)
        cur.execute(sql, datos)
        miConexion.commit()
        miConexion.close()
        mostrardatosMedicos()
        limpiarMedico()


def borrar():
    try:
        name = tabla.item(tabla.selection())
        name = name.get('values')
        name = str(name[0])
    except:
        print("no has seleccionado nada")
    codi = codpaciente.get()
    if (coincidencia(patronCod_Historia, codi) is None):

        messagebox.showerror("Error", "El código paciente debe ser numérico")
    else:
        try:
            if (codi != ""):
                name = codi
            miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
            cur = miConexion.cursor()
            sql = "delete from paciente WHERE codpac = %s"
            datos = name
            cur.execute(sql, datos)
            miConexion.commit()
            miConexion.close()
            mostrardatos()
            limpiar()
        except:
            messagebox.showerror("Error", "no existe ese id")


def borrarMedicos():
    try:
        name = tablaMedicos.item(tablaMedicos.selection())
        name = name.get('values')
        name = str(name[0])
    except:
        print("no has seleccionado nada")
    codi = codmed.get()
    if (coincidencia(patronCod_Historia, codi) is None):
        messagebox.showerror("Error", "El código debe ser numérico")
    else:
        try:
            if (codi != ""):
                name = codi

            miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
            cur = miConexion.cursor()
            sql = "delete from medicos WHERE codmed = %s"
            datos = codi
            cur.execute(sql, datos)
            miConexion.commit()
            miConexion.close()
            mostrardatosMedicos()
            limpiarMedico()
        except:
            messagebox.showerror("Error", "no existe ese id")


def insertarIngresos():
    cd = codingreso.get()
    pr = proc.get()
    fe = fech.get()
    nup = numplan.get()
    nuc = numcam.get()
    ob = observaci.get()
    if (verificacionIngreso(cd, fe, nup, nuc)):
        miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
        cur = miConexion.cursor()
        sql = "INSERT INTO ingresos (coding, procedencia,fecha_ingreso,num_planta,num_cama,observaciones) VALUES (%s,%s,%s,%s,%s,%s)"
        datos = (cd, pr, fe, nup, nuc, ob)
        cur.execute(sql, datos)
        miConexion.commit()
        miConexion.close()
        mostrardatosIngresos()
        limpiaringreso()


def modificarIngresos():
    cd = codingreso.get()
    pr = proc.get()
    fe = fech.get()
    nup = numplan.get()
    nuc = numcam.get()
    ob = observaci.get()
    if (verificacionIngreso(cd, fe, nup, nuc)):
        try:
            name = tablaIngresos.item(tablaIngresos.selection())
            name = name.get('values')
            name = str(name[0])
        except:
            print("no has seleccionado nada")
        codi = codingreso.get()
        try:
            if codi == 0:
                codi = name

            miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
            cur = miConexion.cursor()
            sql = "UPDATE ingresos SET procedencia=%s,fecha_ingreso=%s,num_planta=%s,num_cama=%s,observaciones=%s WHERE coding = %s"
            datos = (pr, fe, nup, nuc, ob, codi)
            cur.execute(sql, datos)
            miConexion.commit()
            miConexion.close()
            mostrardatosIngresos()
            limpiaringreso()
        except:
            messagebox.showerror("Error", "no existe ese id")


def borrarIngresos():
    try:

        name = tablaIngresos.item(tablaIngresos.selection())
        name = name.get('values')
        name = str(name[0])
    except:
        print("no has seleccionado nada")
    codi = codingreso.get()
    if (coincidencia(patronCod_Historia, codi) is None):
        messagebox.showerror("Error", "El código debe ser numérico")
    else:
        try:
            if (codi != ""):
                name = codi
            miConexion = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hospital')
            cur = miConexion.cursor()
            sql = "delete from ingresos WHERE coding = %s"
            datos = codi
            cur.execute(sql, datos)
            miConexion.commit()
            miConexion.close()
            mostrardatosIngresos()
            limpiaringreso()
        except:
            messagebox.showerror("Error", "El id no existe")


ventana = Tk()
ventana.title("Hospital")
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')

# creación de pestañas
pes0 = ttk.Frame(notebook)
pes1 = ttk.Frame(notebook)
pes2 = ttk.Frame(notebook)
notebook.add(pes0, text='Paciente')
notebook.add(pes1, text='Ingresos')
notebook.add(pes2, text='Médico')

# etiquetas paciente
codpa = Label((pes0), text='Codigo pac.').place(x=20, y=10)
numSeg = Label((pes0), text='Nº de Seguridad Social').place(x=20, y=40)
nombre = Label((pes0), text='Nombre').place(x=20, y=70)
apellido = Label((pes0), text='Apellidos').place(x=20, y=100)
domicilio = Label((pes0), text='Domicilio').place(x=20, y=130)
poblacion = Label((pes0), text='Población').place(x=20, y=160)
provincia = Label((pes0), text='Provincia').place(x=20, y=190)
cp = Label((pes0), text='Código postal').place(x=20, y=220)
telefono = Label((pes0), text='Nº de teléfono').place(x=20, y=250)
numHistoria = Label((pes0), text='Nº historial clínico').place(x=20, y=280)
obeserva = Label((pes0), text='Observaciones').place(x=20, y=310)

# etiquetas ingresos
codingres = Label((pes1), text='Codigo ing.').place(x=20, y=10)
proce = Label((pes1), text='Procedencia').place(x=20, y=40)
fecha_ing = Label((pes1), text='Fecha de ingreso').place(x=20, y=70)
num_planta = Label((pes1), text='Número de planta').place(x=20, y=100)
num_cama = Label((pes1), text='Número de cama').place(x=20, y=130)
observa = Label((pes1), text='Observaciones').place(x=20, y=160)
med = Label((pes1), text='Media ingreso/dia').place(x=20, y=190)
por = Label((pes1), text='Porcentaje ingresos/día').place(x=20, y=220)

# variables para recoger el texto
codpaciente = StringVar()
ss = StringVar()
nomb = StringVar()
ape1 = StringVar()
dom = StringVar()
pob = StringVar()
prov = StringVar()
codp = StringVar()
tel = StringVar()
numi = StringVar()
obs = StringVar()

# campos de texto
codpatexto = ttk.Entry(pes0, textvariable=codpaciente).place(x=150, y=10)
numSegText = ttk.Entry(pes0, textvariable=ss).place(x=150, y=40)
nombreTexto = ttk.Entry(pes0, textvariable=nomb).place(x=150, y=70)
apellidoTexto = ttk.Entry(pes0, textvariable=ape1).place(x=150, y=100)
domicilioTexto = ttk.Entry(pes0, textvariable=dom).place(x=150, y=130)
poblacionTexto = ttk.Entry(pes0, textvariable=pob).place(x=150, y=160)
provinciaTexto = ttk.Entry(pes0, textvariable=prov).place(x=150, y=190)
cpTexto = ttk.Entry(pes0, textvariable=codp).place(x=150, y=220)
telefonoTexto = ttk.Entry(pes0, textvariable=tel).place(x=150, y=250)
numHistoriaTexto = ttk.Entry(pes0, textvariable=numi).place(x=150, y=280)
obeservaTexto = ttk.Entry(pes0, textvariable=obs).place(x=150, y=310)

# variables para recoger pestaña ingresos
codingreso = StringVar()
proc = StringVar()
fech = StringVar()
numplan = StringVar()
numcam = StringVar()
observaci = StringVar()
medi = StringVar()
porcen = StringVar()

# campos de texto ingresos
codingTexto = ttk.Entry(pes1, textvariable=codingreso).place(x=150, y=10)
proceTexto = ttk.Entry(pes1, textvariable=proc).place(x=150, y=40)
fechaTexto = ttk.Entry(pes1, textvariable=fech).place(x=150, y=70)
numPlantaTexto = ttk.Entry(pes1, textvariable=numplan).place(x=150, y=100)
numCamaTexto = ttk.Entry(pes1, textvariable=numcam).place(x=150, y=130)
observTexto = ttk.Entry(pes1, textvariable=observaci).place(x=150, y=160)
meddia = ttk.Entry(pes1, textvariable=medi, state=DISABLED).place(x=150, y=190)
porcentaje = ttk.Entry(pes1, textvariable=porcen, state=DISABLED).place(x=150, y=220)

# formación de tabla
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 8))
tabla = ttk.Treeview(pes0, colum=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))

tabla.column(1, width=50)
tabla.column(2, width=60)
tabla.column(3, width=60)
tabla.column(4, width=60)
tabla.column(5, width=60)
tabla.column(6, width=60)
tabla.column(7, width=80)
tabla.column(8, width=60)
tabla.column(9, width=80)
tabla.column(10, width=60)
tabla.column(11, width=90)

tabla.heading(1, text="codpac")
tabla.heading(2, text="numseg")
tabla.heading(3, text="nombre")
tabla.heading(4, text="apellido")
tabla.heading(5, text="domicilio")
tabla.heading(6, text="provincia")
tabla.heading(7, text="poblacion")
tabla.heading(8, text="cp")
tabla.heading(9, text="telefono")
tabla.heading(10, text="numHist")
tabla.heading(11, text="oserva")

tabla['show'] = 'headings'

tabla.bind('<ButtonRelease-1>', seleccion)

# formación de tabla ingresos
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 8))
tablaIngresos = ttk.Treeview(pes1, colum=(1, 2, 3, 4, 5, 6))

tablaIngresos.column(1, width=60)
tablaIngresos.column(2, width=90)
tablaIngresos.column(3, width=90)
tablaIngresos.column(4, width=70)
tablaIngresos.column(5, width=60)
tablaIngresos.column(6, width=90)

tablaIngresos.heading(1, text="coding")
tablaIngresos.heading(2, text="procedencia")
tablaIngresos.heading(3, text="fecha_ingreso")
tablaIngresos.heading(4, text="num_planta")
tablaIngresos.heading(5, text="num_cama")
tablaIngresos.heading(6, text="observaciones")

tablaIngresos.bind('<ButtonRelease-1>', seleccionIngreso)

tablaIngresos['show'] = 'headings'

# botones pacientes

botoninserta = Button(pes0, text="Inserta", command=insertapaciente, height=2, width=7)
botoninserta.place(x=330, y=300)

botonmodifica = Button(pes0, text="Modifica", command=modificapaciente, height=2, width=7)
botonmodifica.place(x=400, y=300)

botonborra = Button(pes0, text="Borra", command=borrar, height=2, width=7)
botonborra.place(x=470, y=300)

botongrafica = Button(pes0, text="Gráfico", command=mostrarGrafica, height=2, width=7)
botongrafica.place(x=540, y=300)

tabla.place(x=40, y=380)

# botones ingresos

botonInsertaIngreso = Button(pes1, text="Insertar", command=insertarIngresos, height=2, width=7)
botonInsertaIngreso.place(x=70, y=270)

botonModificaIngreso = Button(pes1, text="Modificar", command=modificarIngresos, height=2, width=7)
botonModificaIngreso.place(x=150, y=270)

botonBorraIngreso = Button(pes1, text="Borrar", command=borrarIngresos, height=2, width=7)
botonBorraIngreso.place(x=230, y=270)

botonamedia = Button(pes1, text="Media", command=media, height=2, width=7)
botonamedia.place(x=310, y=270)

botonporcen = Button(pes1, text="Porcentaje", command=calcularPorcentaje, height=2, width=7)
botonporcen.place(x=390, y=270)

tablaIngresos.place(x=50, y=350)

print(tabla.selection_set())
print(tabla.focus())
mostrardatos()

print(tablaIngresos.selection_set())
print(tablaIngresos.focus())
mostrardatosIngresos()

# etiquetas medicos
codme = Label((pes2), text='Codigo med.').place(x=20, y=10)
nom = Label((pes2), text='Nombre').place(x=20, y=40)
ape = Label((pes2), text='Apellidos').place(x=20, y=70)
esp = Label((pes2), text='Especialidad').place(x=20, y=100)
num_col = Label((pes2), text='Número de colegiado').place(x=20, y=130)
cargo = Label((pes2), text='Cargo').place(x=20, y=160)
obser = Label((pes2), text='Observaciones').place(x=20, y=190)

# variables para recoger pestaña medicos
codmed = StringVar()
nom = StringVar()
ape = StringVar()
esp = StringVar()
numcol = StringVar()
cargo = StringVar()
obser = StringVar()

# campos de texto medicos
codmedTexto = ttk.Entry(pes2, textvariable=codmed).place(x=150, y=10)
nomTexto = ttk.Entry(pes2, textvariable=nom).place(x=150, y=40)
apeTexto = ttk.Entry(pes2, textvariable=ape).place(x=150, y=70)
espTexto = ttk.Entry(pes2, textvariable=esp).place(x=150, y=100)
numcolTexto = ttk.Entry(pes2, textvariable=numcol).place(x=150, y=130)
cargoTexto = ttk.Entry(pes2, textvariable=cargo).place(x=150, y=160)
obserTexto = ttk.Entry(pes2, textvariable=obser).place(x=150, y=190)

# formación de tabla medicos
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 8))
tablaMedicos = ttk.Treeview(pes2, colum=(1, 2, 3, 4, 5, 6, 7))

tablaMedicos.column(1, width=60)
tablaMedicos.column(2, width=60)
tablaMedicos.column(3, width=60)
tablaMedicos.column(4, width=60)
tablaMedicos.column(5, width=60)
tablaMedicos.column(6, width=60)
tablaMedicos.column(7, width=60)

tablaMedicos.heading(1, text="codmed")
tablaMedicos.heading(2, text="nombre")
tablaMedicos.heading(3, text="apellidos")
tablaMedicos.heading(4, text="especialidad")
tablaMedicos.heading(5, text="num_colegiado")
tablaMedicos.heading(6, text="cargo")
tablaMedicos.heading(7, text="observaciones")

tablaMedicos['show'] = 'headings'

tablaMedicos.bind('<ButtonRelease-1>', seleccionMedico)

# botones medicos

botonInsertaMedico = Button(pes2, text="Insertar", command=insertarMedicos, height=2, width=7)
botonInsertaMedico.place(x=70, y=250)

botonModificaMedico = Button(pes2, text="Modificar", command=modificarMedicos, height=2, width=7)
botonModificaMedico.place(x=150, y=250)

botonBorraMedico = Button(pes2, text="Borrar", command=borrarMedicos, height=2, width=7)
botonBorraMedico.place(x=230, y=250)

tablaMedicos.place(x=90, y=350)

print(tablaMedicos.selection_set())
print(tablaMedicos.focus())
mostrardatosMedicos()

ventana.geometry("800x700")
ventana.mainloop()

import xlsxwriter
import pandas as pd

def ObtenerAsistencias(est,asistencias):

	confirmaciones = [] #Vector que alamcena n's o s's dependiendo de la asistencia

	cols = asistencias.shape[1]

	for i in range(0,cols):

		participantes = list(asistencias.iloc[:,i])

		if est in participantes:
			confirmaciones = confirmaciones + ['s']
		else:
			confirmaciones = confirmaciones + ['n']

	return confirmaciones


asistencias = pd.read_csv('RegDiario.csv' , sep = ',' , dtype = str)
workbook = xlsxwriter.Workbook('Asistencias.xlsx')
worksheet = workbook.add_worksheet()

#Formato de columnas
worksheet.set_column(1,asistencias.shape[1]+1,16)

#Formato de columnas
formato_titulo = workbook.add_format({'bold':True}) #Formato letra en negrita

#Etapa de adjuntar estudiantes a la primera columna
estudiantes =[
	'0107425134',
	'0107252777',
	'0302447156',
	'0105182752',
	'0150548790',
	'0107174013',
	'0106368699',
	'0106055783',
	'0106037302',
	'0150573848',
	'0106427164',
	'0150043685',
	'0105565444',
	'0105994057',
	'0107168320',
	'0106485980',
	'0106122252',
	'0107171803',
	'0106271976',
	'0106139389',
	'0106439094',
	'0107289167',
	'1400814990',
	'0105947378',
	'0705397511',
	'0302447404',
	'0105754618',
	'0105062269',
	'0105142384',
	'0105564546',
	'0105994099',
	'0107378143',
	'0106426208',
	'0604231043',
	'0104728886',
	'0106904675',
	'0302876578',
	'0302707708',
	'0302886577',
	'0150552073',
	'0150547834',
	'0106352784',
	'0302721006',
	'0106765258',
	'0302973417'
	]

#Adjuntar estudiantes numerados a la columna 0 y 1
worksheet.write(0,1,'Estudiantes',formato_titulo)
for i in range(0,len(estudiantes)):
	worksheet.write(i+1,1,str(estudiantes[i])) #Adjuntar N.I
	worksheet.write(i+1,0,i+1) #Numeracion

#Aniadir los dias
next_col = 0
for dia in list(asistencias.columns):
	worksheet.write(0,2+next_col,dia,formato_titulo)
	next_col += 1

#Obtener las asistencias por estudiantes
next_row = 1
for est in estudiantes:
	#Obtener las confirmaciones
	confirmaciones = ObtenerAsistencias(est,asistencias)
	#Aniadir los confimaciones
	next_col = 0
	for conf in confirmaciones:
        	worksheet.write(next_row,2+next_col,conf)
        	next_col += 1

	#Avanzar al siguiente estudiante
	next_row += 1

workbook.close()

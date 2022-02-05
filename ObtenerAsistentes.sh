#!/bin/bash

ObtenerAsistencias(){

	porcentajes=( 50 75 90 ) #Porcentajes de threshold
	img=$1
	i=0

	for p in ${porcentajes[@]}
	do
		convert -threshold ""$p"%" "$img" "TempConvertImg"$i".png"
		tesseract "TempConvertImg"$i".png" "TempTextImg"$i""
		cat "TempTextImg"$i".txt" | egrep -o '[0-9]{10}' >> "TempCedulasTotales.txt"
		rm "TempTextImg"$i".txt"
		rm "TempConvertImg"$i".png"
		i=$((i+1))
	done

	cat TempCedulasTotales.txt | sort | uniq > ParNoVal.txt
	rm TempCedulasTotales.txt
}


ResumirRegistros(){

	dia=$1
	echo "$dia" > "Reg"$dia".txt"
	cat Asis*.txt | sort | uniq >> "Reg"$dia".txt"
	rm Asis*.txt

}


ObtenerRegDiario(){

	dia=$1
	i=0
	for img in `ls . | egrep "$dia" | sed s/\ /\|/g`
	do
		img=`echo "$img" | sed s/\|/\ /g`
		echo "=========Procesando "$img"=========="
		ObtenerAsistencias "$img"
		cat ParNoVal.txt | ./ValidarCedulas.awk >> "Asis"$i".txt"
		rm ParNoVal.txt
		i=$((i+1))
	done

	ResumirRegistros "$dia"

}


Main(){

	#Obtener un registro de participantes por dia
	for dia in `ls . | egrep -o '[0-9]{4}+-+[0-9]{2}+-+[0-9]{2}+' | sort | uniq`
	do
		echo
		echo "Procesando dia:"$dia""
		ObtenerRegDiario "$dia"
	done

	#Generar el archivo .csv que contienes las asistencias diarias
	paste -d , Reg*.txt > RegDiario.csv
	rm Reg*.txt
	python3.8 GenerarRegistros.py
}

Main

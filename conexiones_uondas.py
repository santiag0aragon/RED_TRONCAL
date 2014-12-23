__author__ = 'santiago9101'
import csv


def conexiones_uondas(ciudad, grupo,distancia_max=3):
    file_name = 'Matriz-%s-G%s.csv' % (ciudad, grupo)
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        ciudades_uondas = dict()
        i = 0
        for row in reader:
            #print row
            if i == 0:
                header = row
            conectar_a = ''
            distancia_carretera = ''
            count = 0
            j = 0
            for val in row:
                #print val
                if(val != row[0] and val != '0'and val !=' '):
                    #print "------------- +1------------"
                    count += 1
                    conectar_a = header[j]
                    distancia_carretera = row[j]
                if(val == row[len(row)-1]):
                    #print "ultimo valor de %s %s conexiones"%(row[0],count)
                    if count != 1:
                        conectar_a = ''
                        distancia_carretera = ''
                    ciudades_uondas[row[0]] = [count,conectar_a,distancia_carretera]
                j += 1
            i += 1


    #filtando el dictionario
    ciudades_uondas_fil = dict()
    for item in [i for i in ciudades_uondas.items() if i[1][0] == 1]:
        ciudades_uondas_fil[item[0]] = item[1]



    #print ciudades_uondas_fil




    with open('MAT_FULL_D_NOMBRES.csv', 'rb') as f:
        reader = csv.reader(f)
        mat_d_headers = list(reader)
    ciudades_final = dict()
    for key,val in ciudades_uondas_fil.iteritems():
        c_a = mat_d_headers.index([key])
        c_b = mat_d_headers.index([val[1]])
        ciudades_final[key] = [val[0],val[1],val[2],[c_a,c_b]]
    #print ciudades_final

#consulta de distancias en linea recta
    mat_d = file('MAT_FULL_D.csv', 'r')
    mat_d_lines = mat_d.readlines()
    ciudades_distancia = dict()
    for key,val in ciudades_final.iteritems():
        i = val[3][0]
        j = val[3][1]
        #     Ciudad(indice) ---- Ciudad(indice)
        #     Distancia en linea recta
        #print "%s(%s) --- %s(%s) "%(key,i,val[1],j)
        #print mat_d_lines[i].split(',')[j]

        #CiudadA: [CiudadB,indiceA,indiceB,distancia]
        ciudades_distancia[key] = [val[1],i,j,mat_d_lines[i].split(',')[j]]

    #print ciudades_distancia

    with open('conexiones_uondas.csv', 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.writer(f)
        w.writerow(['CiudadA','CiudadB','IndiceA','IndiceB','Distancia LR','Enlace uOndas ?'])
        for key,val in ciudades_distancia.iteritems():
            enlace_flag = 0
            if float(val[3]) <= distancia_max:
                enlace_flag = 1
            w.writerow([key,val[0],val[1],val[2],val[3],enlace_flag])
if __name__ == "__main__":
    conexiones_uondas('CAMPECHE', '5',3)
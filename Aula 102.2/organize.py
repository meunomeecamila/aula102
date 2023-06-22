import os 
import shutil

#mostrar a pasta de origem para mover as imagens de uma pasta pra outra
from_dir = "C:/Users/apven/OneDrive/Área de Trabalho/PYTHON/Aula 102"
to_dir = "C:/Users/apven/OneDrive/Área de Trabalho/PYTHON/Aula 102.2"

#armazenar os nomes de todos os arquivos
list_of_files = os.listdir(from_dir)

#percorrer o list of files e encontrar extensão dos arquivos
for file_name in list_of_files: 

    name,extension = os.path.splitext(file_name)

    if extension == '':
        continue
#se tiver um dos debaixo, irá mover do from para o to
    if extension in ['.gif','.png','.jpg','.jpeg']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'Arquivos de Imagem'
        path3 = to_dir + '/' + 'Arquivos de Imagem' + '/' + file_name
#verificar se o caminho da pasta existe antes de mover
    if os.path.exists(path2):
        print('Movendo' + file_name + '...')
        #movendo de path1 para path3
        shutil.move(path1, path3)
#se não existir, criar uma nova pasta e mover
    else:
        os.makedirs(path2)
        print('Movendo' + file_name + '...')
        shutil.move(path1, path3)

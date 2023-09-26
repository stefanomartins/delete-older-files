import datetime
import os
import sys

base_dir = sys.argv[1]
n = int(sys.argv[2])


for (root, dirs, files) in os.walk(base_dir, topdown=True):
    for file in files:
        file_path = os.path.join(root, file)

        # Pegando o timestamp da modificação do arquivo e convertendo-o para um objeto datetime
        date_modified_ts = os.path.getmtime(file_path)
        date_modified_dt = datetime.datetime.fromtimestamp(date_modified_ts)

        # Encontrando a quantidade de dias que um arquivo foi modificado
        n_days = (datetime.datetime.now() - date_modified_dt).days

        if n_days > n:
            print(f"Apagando arquivo {file_path}")
            # os.remove(file_path) 


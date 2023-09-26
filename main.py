import datetime
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("base_dir", type=str)
parser.add_argument("-n", action="store", type=int, required=True)
parser.add_argument("--dry-run", action="store_true")

args = parser.parse_args()

base_dir = args.base_dir
n = args.n
dry_run = args.dry_run


for root, dirs, files in os.walk(base_dir, topdown=True):
    for file in files:
        file_path = os.path.join(root, file)

        # Pegando o timestamp da modificação do arquivo e convertendo-o para um objeto datetime
        date_modified_ts = os.path.getmtime(file_path)
        date_modified_dt = datetime.datetime.fromtimestamp(date_modified_ts)

        # Encontrando a quantidade de dias que um arquivo foi modificado
        n_days = (datetime.datetime.now() - date_modified_dt).days

        if n_days > n:

            if dry_run:
                print("Modo dry run ativado")
            else:
                print(f"Apagando arquivo {file_path}")
                os.remove(file_path)

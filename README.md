# delete-older-files

## Descrição
Projeto escrito em Python com o propósito de excluir arquivos mais velhos do que N dias.

## Uso

```bash
python3 main.py base_dir -n n_dias --dry-run
```

Onde:

- base_dir: Diretório onde será realizada a pesquisa.
- -n n_dias: Número de dias desde a última modificação do arquivo. Arquivos mais antigos do que n_dias serão excluídos.
- --dry-run: Caso utilizada, arquivos não serão excluídos.

Exemplos:

```bash
python3 main.py $HOME/Pictures/ -n 10 --dry-run

python3 main.py C:\Data -n 30
```
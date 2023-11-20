# Automatização de processos para renomear imagens

## Objetivo

  O principio básico dessa aplicação tem de reduzir o tempo gasto diariamente com as renomeações dos arquivos em que uso no dia a dia profissional, algumas imagens vem com os caracteres especiais, dificultando assim a importação para ferramentas terceiras. Sendo assim tive obejtivo de criar algo que me ajudaria nessa limpeza de caracteres especiais(--Á, É, Í, Ó, Ú,º, ª--).

## Depêndencias

- Flask: Para esta solução usamos este framework para criar um pequeno servidor WEB para lidar com uploads, renomeação e download de arquivos.
- Os: Foi usado para manipulação dos arquivos usados para upload e download.
- re: Utilizado remove_special_characters para remover caracteres especiais dos nomes de arquivo.

# Bibliotecas 

```
 pip install flask

```
## Usado por

Esse projeto é usado pelas seguintes empresas:

- Softexpert

# Melhorias futuras

-  Tenho como objetivo, adptar um ML para classificar essas alterações de caracteres especiais e também classificar o tipo do arquivo e ajustar o tamanho, para isso estou construindo uma base de aprendizagem para a mesma. Objetivo desta entrega está programada para dia 10/11

## Bibliotecas 

 - scikit-learn


# Mapa de coleta seletiva
O Mapa de Coleta Seletiva é uma aplicação web desenvolvida com Django para exibir e gerenciar pontos de coleta seletiva. O projeto permite que usuários visualizem locais de descarte de resíduos recicláveis e que administradores adicionem ou removam pontos do mapa interativo. 

## Instalação
### Pré-requisitos
Antes de iniciar, certifique-se de ter instalado:
Python
pip
virtualenv

### Clonar o Repositorio do GitHub
git clone https://github.com/FiLpoix/map-coleta-seletiva.git
cd mapa-coleta-seletiva
### Cria o ambiente virtual
python -m venv venv
### Ativar o ambiente virutal
.\venv\Script\activate
### Instalar os pacotes e dependencias
pip install -r .\requirements.txt
### Realizar as migrações
python .\manage.py makemigrations
python .\manage.py migrate
### Criação do superusuario
python .\manage.py createsuperuser
### Start o Projeto
python .\manage.py runserver

### Exibição do Mapa
O mapa interativo é gerado na view mapa, que exibe os pontos com base na API Folium.

### Fluxo de funcionamento do mapa
01. O usuário acessa /mapa/.
02. O backend recupera todos os pontos cadastrados e renderiza um mapa com Folium.
03. O usuário pode clicar nos pontos para ver detalhes
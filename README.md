📚 Django Students API – Desafio Técnico

Projeto desenvolvido como parte de um desafio técnico, com foco em boas práticas, organização de código e testes automatizados.

🚀 Tecnologias utilizadas

Python 3.14

Django

Django REST Framework

SQLite

Coverage (testes)

📂 Funcionalidades

CRUD completo de Students

Relacionamento com Courses e Enrollments

Views tradicionais (Django CBVs)

API REST

Managers e QuerySets customizados

Testes unitários, de views e integração

Cobertura de testes acima de 85%

⚙️ Como rodar o projeto
1️⃣ Clonar o repositório
git clone https://github.com/seuusuario/nome-do-repositorio.git
cd nome-do-repositorio

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv


Windows:

venv\Scripts\activate


Linux / macOS:

source venv/bin/activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Rodar migrações
python manage.py migrate

5️⃣ Iniciar o servidor
python manage.py runserver

🧪 Rodando os testes
Executar testes
python manage.py test

Executar testes com coverage
python -m coverage run manage.py test
python -m coverage report


Cobertura mínima atingida: 87%

🧠 Observações

Pastas como venv/, __pycache__/ e arquivos .coverage não fazem parte do repositório

O projeto está organizado para facilitar manutenção e escalabilidade

Código escrito seguindo boas práticas do Django

👤 Autor

João Pedro Silva
Desenvolvedor Django

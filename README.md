# Tutorial para rodar o projeto:

## Dependências:
- venv
- streamlit

## Como rodar:
### Começando um ambiente virtual:
```bash
cd meuProjeto
```

```bash
python -m venv .venv
```

Uma pasta .venv foi criada no diretório raiz.

#### Para ativar o ambiente:

```bash
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```

Para instalar as depedências dentro do seu .venv utilize:
```bash
pip install -r requirements.txt
```

Agora inicie o projeto com:
```bash
streamlit run index.py
```
# Olist

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Dataset publico de e-commerce Brasileiro

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         module_olist and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── module_olist   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes module_olist a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------



# OLIST - Machine Learning

## Status do Projeto

Projeto iniciado e ambiente de desenvolvimento configurado.

### Ambiente

- Python: 3.13
- Gerenciamento de dependências: UV
- Ambiente virtual: `.venv`
- Dependências controladas por:
  - `pyproject.toml`
  - `uv.lock`

# ------------------------------------------------------------------------
# README — Configuração do Ambiente Python com `uv` e Jupyter

Este projeto utiliza `uv` para gerenciamento de ambiente e dependências.

## 1. Entrar na pasta do projeto

No terminal:

```powershell
cd caminho\do\projeto
```

Exemplo:

```powershell
cd C:\Users\usuario\Documents\Machine-Learning\olist\olist
```

## 2. Sincronizar as dependências

Execute:

```powershell
uv sync
```

O `uv sync` utiliza:

* `pyproject.toml`
* `uv.lock`
* `.python-version`

para recriar o ambiente do projeto com as dependências e versões corretas.

## 3. Ativar a `.venv`

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Depois da ativação, o terminal deve mostrar o ambiente no início da linha, por exemplo:

```text
(olist) PS C:\...\olist\olist>
```

## 4. Conferir a versão do Python

Execute:

```powershell
python --version
```

Este projeto utiliza Python `3.13.x`.

Também confirme qual executável está sendo utilizado:

```powershell
python -c "import sys; print(sys.executable)"
```

O caminho deve apontar para:

```text
...\olist\olist\.venv\Scripts\python.exe
```

## 5. Registrar o ambiente como kernel do Jupyter

Para garantir que o VS Code utilize exatamente a `.venv` do projeto nos notebooks, registre manualmente o kernel:

```powershell
python -m ipykernel install --user --name olist-py313 --display-name "OLIST (Python 3.13.15)"
```

Esse passo é importante principalmente ao configurar o projeto em uma nova máquina.

## 6. Selecionar o kernel no VS Code

Abra o arquivo `.ipynb`.

No canto superior direito:

```text
Select Kernel
```

Selecione:

```text
OLIST (Python 3.13.15)
```

Caso não apareça imediatamente, recarregue o VS Code:

```text
Ctrl + Shift + P
Developer: Reload Window
```

Depois tente selecionar o kernel novamente.

## 7. Confirmar o ambiente dentro do notebook

Execute uma célula com:

```python
import sys

print(sys.executable)
print(sys.version)
```

O resultado deve apontar para a `.venv` do projeto e para Python `3.13.x`.

Exemplo:

```text
C:\Users\usuario\Documents\Machine-Learning\olist\olist\.venv\Scripts\python.exe

3.13.15 ...
```

## 8. Testar as principais dependências

Para verificar o `data_profiling`:

```powershell
python -c "from data_profiling import ProfileReport; print('OK')"
```

Se aparecer:

```text
OK
```

a biblioteca está corretamente instalada.

Também pode ser testado diretamente no notebook:

```python
from data_profiling import ProfileReport
import ipywidgets

print("Tudo OK")
```

---

# Configuração em uma nova máquina

Sempre que este projeto for utilizado em outro computador, seguir esta sequência:

```text
1. Clonar o repositório
2. Entrar na pasta correta do projeto
3. Executar uv sync
4. Ativar a .venv
5. Conferir python --version
6. Conferir sys.executable
7. Registrar o kernel com ipykernel
8. Selecionar o kernel correto no VS Code
9. Testar as dependências
```

Comandos principais:

```powershell
uv sync

.\.venv\Scripts\Activate.ps1

python --version

python -c "import sys; print(sys.executable)"

python -m ipykernel install --user --name olist-py313 --display-name "OLIST (Python 3.13.15)"

python -c "from data_profiling import ProfileReport; print('OK')"
```

## Atenção

O ambiente virtual `.venv` e o kernel utilizado pelo Jupyter são coisas diferentes.

Mesmo que a `.venv` esteja utilizando corretamente Python 3.13, o VS Code pode continuar mostrando um kernel antigo, por exemplo Python 3.14.

Nesse caso, registrar manualmente o kernel com:

```powershell
python -m ipykernel install --user --name olist-py313 --display-name "OLIST (Python 3.13.15)"
```

e selecioná-lo no notebook resolve o problema.

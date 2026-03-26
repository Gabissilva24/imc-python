# IMC Python

Aplicação web para cálculo de IMC (Índice de Massa Corporal) desenvolvida com Python e Flask.

## Pré-requisitos

- [Python 3.x](https://www.python.org/downloads/) instalado e adicionado ao PATH
- [Git](https://git-scm.com/downloads) instalado

Verifique as instalações abrindo o **Prompt de Comando (cmd)** e executando:

```cmd
python --version
git --version
```

## Como rodar o projeto

### 1. Clone o repositório

```cmd
git clone https://github.com/GTI-Fatec-Jahu/imc-python.git
cd imc-python
```

### 2. Crie o ambiente virtual (venv)

```cmd
python -m venv venv
```

### 3. Ative o ambiente virtual

**Prompt de Comando (cmd):**
```cmd
venv\Scripts\activate
```

**PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

> Se o PowerShell bloquear a execução, rode antes:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

Após ativar, o terminal exibirá `(venv)` no início da linha.

### 4. Instale as dependências

```cmd
pip install -r requirements.txt
```

### 5. Execute a aplicação

```cmd
python app.py
```

A aplicação estará disponível em: **http://127.0.0.1:5000**

---

### Desativar o ambiente virtual

Ao terminar, desative o venv com:

```cmd
deactivate
```

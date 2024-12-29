# ☕ **Flask Cafe API**

Uma API desenvolvida com **Flask** e **SQLAlchemy** para gerenciar um banco de dados de cafés. A API permite adicionar, consultar, atualizar e excluir informações sobre cafés.

## 📚 **Índice**
1. [Tecnologias Usadas](#-tecnologias-usadas)
2. [Instalação](#-instalação)
3. [Rotas da API](#-rotas-da-api)
4. [Exemplos de Uso](#-exemplos-de-uso)
5. [Contribuição](#-contribuição)
6. [Licença](#-licença)

---

## 🛠️ **Tecnologias Usadas**

- Python
- Flask
- SQLAlchemy
- SQLite
- Jinja2

---

## 🚀 **Instalação**

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/flask-cafe-api.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd flask-cafe-api
   ```
3. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o servidor:
   ```bash
   flask run
   ```

O servidor rodará em `http://127.0.0.1:5000/`.

---

## 🌍 **Rotas da API**

### 🔹 **GET /random**
- Retorna um café aleatório do banco de dados.

### 🔹 **GET /search/&lt;location&gt;**
- Busca cafés com base na localização.

### 🔹 **GET /all**
- Retorna todos os cafés cadastrados.

### 🔹 **POST /add**
- Adiciona um novo café.
- **Parâmetros:** `name`, `map_url`, `img_url`, `location`, `seats`, `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls`, `coffee_price`

### 🔹 **PATCH /update-price/&lt;cafe_id&gt;**
- Atualiza o preço de um café.
- **Parâmetros:** `new_price`

### 🔹 **DELETE /report-closed/&lt;cafe_id&gt;**
- Remove um café do banco de dados.
- **Parâmetros:** `api_key`

---

## 📊 **Exemplos de Uso**

### ✅ **Adicionar um Café (POST)**
```bash
curl -X POST http://127.0.0.1:5000/add -d "name=Gustavo Cafe" -d "map_url=http://map.url" -d "img_url=http://img.url" -d "location=Brasilia" -d "seats=80" -d "has_toilet=true" -d "has_wifi=true" -d "has_sockets=true" -d "can_take_calls=true" -d "coffee_price=$4.50"
```

### ✅ **Atualizar Preço (PATCH)**
```bash
curl -X PATCH http://127.0.0.1:5000/update-price/1 -d "new_price=$5.00"
```

### ✅ **Deletar um Café (DELETE)**
```bash
curl -X DELETE "http://127.0.0.1:5000/report-closed/1?api_key=TopSecretAPIKey"
```

---

## 🤝 **Contribuição**

1. Faça um Fork do projeto.
2. Crie uma branch para sua funcionalidade:
   ```bash
   git checkout -b minha-funcionalidade
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Envie para o repositório:
   ```bash
   git push origin minha-funcionalidade
   ```
5. Abra um Pull Request.

---

## 📄 **Licença**

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido com 💻🤖 e ☕ por [Gustavo Antonio](https://github.com/gus-ant)** 🚀


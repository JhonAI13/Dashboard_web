# Dashboard_web
 # Análise de Veículos com Streamlit

Este projeto é uma aplicação interativa desenvolvida em Python utilizando **Streamlit** para explorar um conjunto de dados de veículos. A ferramenta permite a visualização e análise dos dados por meio de histogramas, scatter plots, estatísticas descritivas e um mapa de calor da correlação.

## 📌 Funcionalidades
- **Visualização dos Dados**: Exibição da base de dados completa.
- **Histograma Interativo**: Permite selecionar uma coluna numérica (preço, ano, odômetro, dias) e visualizar sua distribuição.
- **Scatter Plot Dinâmico**: Escolha interativa das variáveis para os eixos X e Y, analisando relações entre atributos numéricos.
- **Estatísticas Descritivas**: Exibe métricas como média, desvio padrão e quartis para melhor compreensão dos dados.
- **Mapa de Calor da Correlação**: Gera um heatmap das correlações entre variáveis numéricas com opção de download da imagem.

## 📂 Estrutura do Projeto
```
/
├── app.py                # Arquivo principal da aplicação Streamlit
├── data/
│   ├── vehicles.csv      # Base de dados utilizada na análise
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
```

## 🚀 Como Executar
### 1️⃣ Instale as dependências
Certifique-se de que possui o Python instalado e execute:
```bash
pip install -r requirements.txt
```

### 2️⃣ Execute a aplicação
```bash
streamlit run app.py
```

Acesse no navegador:
```
http://localhost:8501
```

## 🔧 Dependências
As principais bibliotecas utilizadas são:
- **Streamlit** (interface interativa)
- **Pandas** (manipulação de dados)
- **NumPy** (operações matemáticas)
- **Matplotlib** (visualização de dados)

Instale todas as dependências com:
```bash
pip install -r requirements.txt
```

## 📌 Observações
- Certifique-se de que o arquivo `vehicles.csv` está presente na pasta `data/`.
- Se estiver rodando no **Render**, não defina manualmente `serverAddress` e `serverPort`, pois a plataforma configura isso automaticamente.

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para modificar e utilizar conforme necessário.

---
Desenvolvido com ❤️ usando Python & Streamlit 🚀


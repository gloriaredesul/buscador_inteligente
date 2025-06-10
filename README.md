# 🔎 Buscador de Nomes em Planilhas Excel

Este projeto em Python permite que você **carregue várias planilhas Excel (`.xlsx`)**, **busque nomes específicos dentro delas** e veja **em quais arquivos esses nomes aparecem**. É ideal para quem precisa cruzar informações em vários arquivos, como listas de presença, cadastros ou relatórios.

---

## 🧠 O que você vai aprender com este projeto?

* Como **abrir arquivos Excel** com `pandas`
* Criar interfaces simples com `tkinter` (caixas de seleção e entrada)
* Armazenar dados em **cache com `pickle`**
* Praticar estruturas como **dicionários**, **loops**, **funções** e **tratamento de erros**

---

## 🚀 Como usar

### Pré-requisitos

Você precisa ter o Python instalado (versão 3.6 ou superior) e a biblioteca `pandas`.

Instale o `pandas` com o comando:

```bash
pip install pandas
```

---

### Passo a passo

1. **Execute o script** `buscador_planilhas.py` (ou outro nome que você tenha dado a ele).

2. Uma janela será aberta pedindo para você **selecionar os arquivos `.xlsx`**.

3. O programa irá **carregar todas as abas de cada planilha** e salvar em cache (em um arquivo chamado `cache_planilhas.pkl`) para facilitar buscas futuras.

4. Depois, você digita o **nome que deseja buscar** (por exemplo, “joão” ou “maria”).

5. O programa informa em quais arquivos o nome foi encontrado!

---

## 💡 Como o código funciona?

### Principais funções:

#### `carregar_planilhas()`

* Abre uma janela para você selecionar arquivos Excel.
* Lê todas as abas de cada arquivo com `pandas`.
* Salva tudo em um dicionário: `{nome_do_arquivo: [dataframes_de_cada_aba]}`.

#### `salvar_cache()` e `carregar_cache()`

* Salvam e recuperam os dados carregados para não precisar abrir tudo de novo toda vez.

#### `buscar_nome()`

* Procura o nome (em letras minúsculas) dentro de todos os arquivos e abas.
* Retorna uma lista com os nomes dos arquivos onde o nome foi encontrado.

#### `iniciar_busca()`

* É o ponto de entrada.
* Pergunta se você quer usar o cache ou carregar os arquivos de novo.
* Permite fazer buscas repetidas até você digitar “nada”.

---

## 🖼️ Exemplo prático

Imagine que você tem 3 arquivos Excel com várias abas, e quer saber **em quais planilhas aparece o nome "ana"**.

Este script te ajuda a descobrir isso **sem precisar abrir cada arquivo manualmente**.

---

## 🧼 Dicas para iniciantes

* Este projeto usa **interface gráfica com janelas simples**, então não precisa saber interface web nem terminal avançado.
* Se quiser adaptar, você pode adicionar filtros, salvar os resultados em um arquivo `.txt` ou mostrar em uma tabela interativa.

---

## 📁 Estrutura dos arquivos

```
seu_projeto/
│
├── buscador_planilhas.py     ← O script principal
├── cache_planilhas.pkl       ← Cache automático dos dados (criado após rodar)
```

---

## 📌 Possíveis melhorias

* Suporte a arquivos `.xls` e `.csv`
* Mostrar em qual aba o nome foi encontrado
* Interface gráfica mais completa (com botões e layout)

---

## 📚 Referências

* [Documentação do pandas](https://pandas.pydata.org/docs/)
* [Tkinter – Interfaces gráficas com Python](https://docs.python.org/pt-br/3/library/tkinter.html)
* [pickle – Serialização de objetos em Python](https://docs.python.org/3/library/pickle.html)

---

## 🤝 Contribuições

Este projeto é um ótimo ponto de partida para quem está começando com automação de planilhas em Python. Fique à vontade para estudar, modificar e adaptar conforme sua necessidade!


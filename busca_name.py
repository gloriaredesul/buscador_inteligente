import pandas as pd
from tkinter import Tk, filedialog, simpledialog, messagebox
import os
import pickle

CACHE_FILE = "cache_planilhas.pkl"

def salvar_cache(dados):
    with open(CACHE_FILE, "wb") as f:
        pickle.dump(dados, f)

def carregar_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "rb") as f:
            return pickle.load(f)
    return None

def carregar_planilhas():
    root = Tk()
    root.withdraw()

    arquivos = filedialog.askopenfilenames(
        title="Selecione os arquivos .xlsx",
        filetypes=[("Arquivos Excel", "*.xlsx")]
    )

    if not arquivos:
        messagebox.showinfo("Nenhum arquivo selecionado", "Você não selecionou nenhum arquivo.")
        return None

    dados_planilhas = {}

    for caminho in arquivos:
        try:
            xls = pd.ExcelFile(caminho)
            dados_arquivo = []
            for nome_aba in xls.sheet_names:
                df = xls.parse(nome_aba)
                dados_arquivo.append(df)
            dados_planilhas[os.path.basename(caminho)] = dados_arquivo
        except Exception as e:
            print(f"Erro ao carregar {caminho}: {e}")

    print(f"\n✅ {len(dados_planilhas)} arquivos carregados com sucesso.\n")
    salvar_cache(dados_planilhas)
    return dados_planilhas

def buscar_nome(dados_planilhas, nome_busca):
    encontrados = []

    for nome_arquivo, lista_abas in dados_planilhas.items():
        for df in lista_abas:
            if df.astype(str).apply(lambda x: x.str.lower()).isin([nome_busca]).any().any():
                encontrados.append(nome_arquivo)
                break

    return encontrados

def iniciar_busca():
    root = Tk()
    root.withdraw()

    dados_planilhas = carregar_cache()

    if dados_planilhas:
        resposta = messagebox.askyesno(
            "Cache encontrado",
            "Cache de arquivos carregados encontrado.\nDeseja usar os arquivos carregados anteriormente?"
        )
        if not resposta:
            dados_planilhas = carregar_planilhas()
    else:
        dados_planilhas = carregar_planilhas()

    if not dados_planilhas:
        return

    while True:
        nome_busca = simpledialog.askstring("Buscar Nome", "Digite o nome que deseja buscar (ou deixe em branco para sair):")
        if not nome_busca:
            print("\nEncerrando busca.")
            break

        nome_busca = nome_busca.strip().lower()
        encontrados = buscar_nome(dados_planilhas, nome_busca)

        if encontrados:
            resultado = f"\n✅ Nome '{nome_busca}' encontrado nos arquivos:\n" + "\n".join(f"- {nome}" for nome in encontrados)
        else:
            resultado = f"\n❌ Nome '{nome_busca}' não encontrado em nenhum dos arquivos."

        print(resultado)
        messagebox.showinfo("Resultado da busca", resultado)

if __name__ == "__main__":
    iniciar_busca()

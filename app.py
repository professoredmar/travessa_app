from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def load_travessas():
    """Carrega os dados dos JSONs"""
    travessas = {}
    try:
        with open('data/travessas.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON: {str(e)}")
    
    try:
        with open('data/travessas_extra.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON EXTRA: {str(e)}")
    
    try:
        with open('data/travessas_extra2.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON EXTRA2: {str(e)}")
    
    try:
        with open('data/lista_J.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_J: {str(e)}")
    
    try:
        with open('data/lista_jj.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_JJ: {str(e)}")
    
    try:
        with open('data/lista_jr.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_JR: {str(e)}")
    
    try:
        with open('data/lista_jl.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_JL: {str(e)}")
    
    try:
        with open('data/lista_jm.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_JM: {str(e)}")
    
    try:
        with open('data/lista_m.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_M: {str(e)}")
    
    try:
        with open('data/lista_mm.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_MM: {str(e)}")
    
    try:
        with open('data/lista_mn.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_MN: {str(e)}")
    
    try:
        with open('data/lista_no.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_NO: {str(e)}")
    
    try:
        with open('data/lista_or.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_OR: {str(e)}")
    
    try:
        with open('data/lista_rs.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_RS: {str(e)}")
    
    try:
        with open('data/lista_st.json', 'r', encoding='utf-8') as f:
            travessas.update(json.load(f))
    except Exception as e:
        print(f"ERRO AO LER JSON LISTA_ST: {str(e)}")
    
    return travessas

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/buscar", methods=["POST"])
def buscar():
    try:
        termo = request.form.get("nome_travessa", "").lower()
        palavras = termo.split()
        travessas = load_travessas()

        resultados = []
        for chave, valor in travessas.items():
            if all(palavra in chave for palavra in palavras):
                resultados.append(valor)

        return jsonify({"resultados": resultados})
    except Exception as e:
        print(f"ERRO NA BUSCA: {str(e)}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

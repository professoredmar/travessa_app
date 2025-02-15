from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def load_travessas():
    """Carrega os dados do JSON"""
    try:
        with open('data/travessas.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"ERRO AO LER JSON: {str(e)}")
        return {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/buscar", methods=["POST"])
def buscar():
    try:
        termo = request.form.get("nome_travessa", "").lower()
        travessas = load_travessas()

        resultados = [valor for chave, valor in travessas.items() if termo in chave]
        return jsonify({"resultados": resultados})
    except Exception as e:
        print(f"ERRO NA BUSCA: {str(e)}")
        return jsonify({"erro": "Erro interno no servidor"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

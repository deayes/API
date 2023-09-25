from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/gerar_texto', methods=['POST'])
def gerar_texto():

    # Exemplo de resposta
    return jsonify({'texto_generado': 'Exemplo de texto gerado'})

@app.route('/chat_gpt', methods=['POST'])
def chat_gpt():
    prompt = request.json['prompt']

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )

    return jsonify({'resposta_gpt': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)

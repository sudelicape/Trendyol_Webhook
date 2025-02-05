from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Trendyol'dan gelen veriyi al
    print("Webhook Received:", data)  # Konsola yazdır (test amaçlı)
    
    # Burada Trendyol verisini işleyebilir ve gerekli aksiyonları alabilirsin

    return jsonify({"message": "Webhook received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

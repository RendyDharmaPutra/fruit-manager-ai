from flask import Flask, request, jsonify
from services.price_calculator import calculate_total_price
from services.holiday_checker import is_holiday
from services.model_service import load_model, predict_percentages
from utils.file_utils import append_to_csv, git_commit_and_push
import numpy as np



app = Flask(__name__)
model = load_model()

@app.route("/price", methods=['POST'])
def calculate_price():
    try:
        data = request.json
        fruit_weights = float(data.get('totalWeight'))
        distance = float(data.get('distance'))
        fuel_price = float(data.get('fuelPrice'))
        weather = int(data.get('weather'))
        date = data.get('transactionTime')

        is_public_holiday = is_holiday(date)
        total_fruit_price = data.get("totalPrice")

        # Hanya hitung sekali jika < 10
        percentages = None
        if distance < 10:
            percentages = predict_percentages(
                model, fruit_weights, distance, fuel_price, weather, is_public_holiday
            )

        total_price = round(calculate_total_price(
            fruit_weights, distance, fuel_price, weather,
            is_public_holiday, total_fruit_price, model, percentages
        ))

        # Simpan ke CSV hanya jika < 10
        if percentages is not None:
            append_to_csv([
                fruit_weights, distance, fuel_price, weather, is_public_holiday,
                percentages[0], percentages[1]
            ])
            git_commit_and_push()

        return jsonify({'total_harga': total_price})

    except Exception as e:
        return jsonify({'error': 'Terjadi kesalahan pada server.', 'detail': str(e)}), 500




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

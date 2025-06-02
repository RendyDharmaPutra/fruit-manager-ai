from .model_service import predict_percentages

def calculate_transport_cost(distance, fuel_price):
    fuel_per_km = 1 / 40
    return distance * fuel_price * fuel_per_km

def calculate_total_price(
    fruit_weights, distance, fuel_price, weather, holiday,
    fruit_price, model, percentages=None
):
    transport_cost = calculate_transport_cost(distance, fuel_price)

    if distance >= 10:
        holiday_cost = fruit_price * 0.03 if holiday else 0
        weather_cost = fruit_price * (0.03 if weather == 1 else 0.01)
    else:
        if percentages is None:
            percentages = predict_percentages(model, fruit_weights, distance, fuel_price, weather, holiday)
        weather_cost = fruit_price * (percentages[0] / 100)
        holiday_cost = fruit_price * (percentages[1] / 100) if holiday else 0

    total = fruit_price + transport_cost + holiday_cost + weather_cost
    return total

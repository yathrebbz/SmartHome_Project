import pandas as pd


def analyze():

    data = pd.read_csv("data/sensor_data.csv")

    print("=" * 60)
    print("           SMART HOME DATA ANALYSIS")
    print("=" * 60)

    print(f"📊 Nombre total de mesures : {len(data)}")

    print("\n🌡️ Température")
    print(f"   • Moyenne   : {data['Temperature'].mean():.2f} °C")
    print(f"   • Maximale  : {data['Temperature'].max():.2f} °C")
    print(f"   • Minimale  : {data['Temperature'].min():.2f} °C")

    print("\n💧 Humidité")
    print(f"   • Moyenne   : {data['Humidity'].mean():.2f} %")
    print(f"   • Maximale  : {data['Humidity'].max()} %")
    print(f"   • Minimale  : {data['Humidity'].min()} %")

    print("\n💡 Luminosité")
    print(f"   • Moyenne   : {data['Light'].mean():.2f} lux")
    print(f"   • Maximale  : {data['Light'].max()} lux")
    print(f"   • Minimale  : {data['Light'].min()} lux")

    print("\n🚶 Mouvement")
    print(f"   • Nombre de mouvements détectés : {data['Motion'].sum()}")

    print("\n📈 Statistiques complètes")
    print(data.describe())

    print("=" * 60)


if __name__ == "__main__":
    analyze()
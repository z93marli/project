import requests
from datetime import datetime

# Välj elområde: "SE1", "SE2", "SE3" eller "SE4"
EL_AREA = "SE3"

def get_today_elpriser(area: str):
    """Hämta dagens elpriser för valt elområde från elprisetjustnu.se API."""
    today = datetime.now()
    date_str = today.strftime("%Y/%m-%d")  # API-format: YYYY/MM-DD
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{date_str}_{area}.json"

    resp = requests.get(url, timeout=10)
    resp.raise_for_status()   # Kasta fel om något går snett

    return resp.json()        # Lista med timpriser (dicts)


def find_current_price(price_list):
    """Hitta priset för aktuell timme i listan från API:et."""
    now = datetime.now()
    current_hour = now.hour

    for entry in price_list:
        # "time_start" är t.ex. "2026-01-02T17:00:00"
        start = datetime.fromisoformat(entry["time_start"])
        if start.hour == current_hour:
            return entry

    return None


def main():
    try:
        prices = get_today_elpriser(EL_AREA)
    except Exception as e:
        print("Kunde inte hämta elpris:", e)
        return

    current = find_current_price(prices)

    print(f"Elområde: {EL_AREA}")
    print("-" * 40)

    if current:
        now_price_ore = round(current["SEK_per_kWh"] * 100, 1)
        print("Aktuellt timpris:")
        print(f"  Från {current['time_start']} till {current['time_end']}")
        print(f"  Pris: {now_price_ore} öre/kWh\n")
    else:
        print("Hittade inget pris för den aktuella timmen.\n")

    print("Alla timpriser idag:")
    for entry in prices:
        start = entry["time_start"]
        price_ore = round(entry["SEK_per_kWh"] * 100, 1)
        print(f"{start}: {price_ore:5.1f} öre/kWh")


if __name__ == "__main__":
    main()
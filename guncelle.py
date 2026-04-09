import pandas as pd
import requests
import io
import json

# Sizin paylaştığınız CSV linki
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSUzP0agyoHmSc3tDZSqiDs1PIlWDeRSou6k4ybBQAQ6NaGm-EE6Ox31taSrZezZROsbyWIpwS0xHtk/pub?gid=1751503618&single=true&output=csv"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'
    df = pd.read_csv(io.StringIO(response.text))
    
    # Sütun isimlerindeki boşlukları temizleyelim
    df.columns = df.columns.str.strip()
    
    # JSON formatına çevirip kaydedelim
    data_list = df.to_dict(orient='records')
    with open('veriler.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
        
    print("Veri başarıyla güncellendi!")
except Exception as e:
    print(f"Hata: {e}")

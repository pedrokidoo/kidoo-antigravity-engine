import urllib.request
import ssl
import re

ctx = ssl._create_unverified_context()

for path in ["/", "/contato"]:
    url = "https://www.kidoohub.com.br" + path
    print(f"\n=== URL: {url} ===")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx) as r:
            html = r.read().decode("utf-8", errors="ignore")
            print("Status:", r.status)
            
            # Procura por inputs dentro do form
            inputs = re.findall(r'<input[^>]*>|<textarea[^>]*>', html)
            for inp in inputs:
                print("Campo Form:", inp[:150])
            buttons = re.findall(r'<button[^>]*>(.*?)</button>', html, re.DOTALL)
            for b in buttons:
                print("Botão Form:", re.sub(r'<[^>]+>', '', b).strip()[:50])
    except Exception as e:
        print("Erro:", e)

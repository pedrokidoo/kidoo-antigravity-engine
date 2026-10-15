import urllib.request
import ssl
import re
import json

ctx = ssl._create_unverified_context()

def check_login():
    print("--- 1. Verificando Healthcheck da API ---")
    req = urllib.request.Request("https://crm-kidoo.vercel.app/api/v1/health", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, context=ctx) as r:
            print("Status API:", r.status, r.read().decode())
    except Exception as e:
        print("Erro Health:", e)

    supabase_url = "https://ujjnslintpuzaqvsphsh.supabase.co"
    supabase_key = "sb_publishable_WfENXMNo72h3_-aPaxcqOg_RypDlSuL"
    print("Supabase URL:", supabase_url)
    print("Supabase Key:", supabase_key)
    if supabase_url and supabase_key:
        print("Supabase Key encontrada:", supabase_key[:25] + "...")
        print("\n--- 3. Testando Login com credenciais do Erick ---")
        login_url = f"{supabase_url}/auth/v1/token?grant_type=password"
        payload = json.dumps({
            "email": "rizarezende2020@gmail.com",
            "password": "814841Riza@"
        }).encode("utf-8")
        login_req = urllib.request.Request(
            login_url,
            data=payload,
            headers={
                "apikey": supabase_key,
                "Content-Type": "application/json"
            }
        )
        try:
            with urllib.request.urlopen(login_req, context=ctx) as r:
                auth_data = json.loads(r.read().decode())
                print(">>> LOGIN COM SUCESSO! <<<")
                print("User ID:", auth_data.get("user", {}).get("id"))
                print("Email:", auth_data.get("user", {}).get("email"))
                token = auth_data.get("access_token")

                print("\n--- 4. Testando Consulta ao Perfil do Usuário na API (/users/me) ---")
                me_req = urllib.request.Request(
                    "https://crm-kidoo.vercel.app/api/v1/users/me",
                    headers={
                        "Authorization": f"Bearer {token}",
                        "User-Agent": "Mozilla/5.0"
                    }
                )
                try:
                    with urllib.request.urlopen(me_req, context=ctx) as r_me:
                        print("Perfil retornado com sucesso!", r_me.status, r_me.read().decode())
                except urllib.error.HTTPError as e_me:
                    print("Erro ao buscar perfil (/users/me):", e_me.code, e_me.read().decode())
        except urllib.error.HTTPError as e:
            print("Erro no Login do Supabase:", e.code, e.read().decode())

if __name__ == "__main__":
    check_login()

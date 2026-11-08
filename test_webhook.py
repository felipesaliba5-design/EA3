"""
Script de teste de comunicação HTTP com o Webhook do n8n
Agente: EduBot — Assistente Virtual DevAcademy
"""

import sys
import uuid
import json

# URL oficial do n8n Cloud ou Local
DEFAULT_WEBHOOK_URL = "https://n8n.incluc0de.com.br/webhook/chat"
LOCAL_WEBHOOK_URL = "http://localhost:5678/webhook/chat"

def send_message(message: str, session_id: str = None, webhook_url: str = DEFAULT_WEBHOOK_URL):
    try:
        import requests
    except ImportError:
        print("[!] Biblioteca 'requests' não encontrada. Instale com: pip install requests")
        return

    if session_id is None:
        session_id = f"sessao_edubot_{uuid.uuid4().hex[:8]}"
    
    payload = {
        "message": message,
        "session_id": session_id
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    print(f"\n[*] Endpoint: {webhook_url}")
    print(f"[*] Payload ({session_id}): {message}")
    
    try:
        response = requests.post(webhook_url, json=payload, headers=headers, timeout=60)
        print(f"[*] Status HTTP: {response.status_code}")
        
        if response.status_code == 200:
            print("[+] Resposta do EduBot:")
            data = response.json()
            if isinstance(data, dict) and "output" in data:
                print(f"\n{data['output']}\n")
            else:
                print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            print(f"[-] Erro retornado ({response.status_code}): {response.text}")
            
    except Exception as e:
        print(f"[-] Falha na requisição: {e}")

if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_WEBHOOK_URL
    session = f"aluno_teste_{uuid.uuid4().hex[:6]}"
    
    print("=" * 60)
    print(f"TESTE DE INTEGRAÇÃO EDUBOT -> WEBHOOK N8N")
    print(f"URL Alvo: {target_url}")
    print("=" * 60)
    
    print("\n--- CASO 1: Consulta de Prazo Oficial (Bootcamp Front-End React) ---")
    send_message(
        message="Qual é a data limite para a entrega do projeto final do Bootcamp Front-End React?",
        session_id=session,
        webhook_url=target_url
    )



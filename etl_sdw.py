import pandas as pd
import random
import openai

df = pd.read_csv(r'SDW2025.csv')
print(f'Dados importados com sucesso!\nTotal de registros: {len(df)}')
users_id  = df['UserID'].tolist()

'''def generate_ai_news_mock(name, status):
    features = {
        "Gold": "investimento exclusivo",
        "Platinum": "concierge e salas VIP",
        "Standard": "taxa zero em transferências"
    }
    benefit = features.get(status, "nossos serviços")
    return f"Olá {name}, aproveite os {benefit} do seu plano Santander {status}!"'''

# Função real (Descomente se tiver a API Key da OpenAI)
def generate_ai_news_openai(user):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Você é um especialista em marketing bancário."},
        {"role": "user", "content": f"Crie uma mensagem curta para {user['Name']} sobre investimentos."}
      ]
    )
    return completion.choices[0].message.content.strip()

print("\n🤖 Iniciando Transformação (Gerando mensagens com IA)...")

news = []
for index, row in df.iterrows():
    # AQUI: Se tiver a API Key, troque pela função generate_ai_news_openai
    message = generate_ai_news_openai(row)
    news.append(message)
    print(f"Usuário {row['Name']}: {message}")

df['News'] = news

print("\n📤 Iniciando Carregamento...")
try:
    df.to_csv('SDW2023_ENRICHED.csv', index=False)
    print("Sucesso! O arquivo 'SDW2023_ENRICHED.csv' foi criado com as mensagens.")
except Exception as e:
    print(f"Erro ao salvar: {e}")
from faker import Faker
import pandas as pd


fake = Faker('pt_BR')

def persona(quantidade):
    personas = []
    for _ in range(quantidade):
        data = {
            'nome': fake.name(),
            'endereco': fake.address(),
            'email': fake.email(),
        }
        personas.append(data)

    print(f'Foram adicionadas {quantidade} personas.')
    
    # Transforma a lista de dicionários em um DataFrame
    df = pd.DataFrame(personas)
    
    
    
    return df
result = persona(20)

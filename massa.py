from faker import Faker

fake = Faker('pt_BR')
print(fake.name())  # Gera um nome aleatório
print(fake.text())  # Gera um endereço aleatório
print(fake.email())

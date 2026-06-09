import pandas as pd

def get_dados_monitoramento(): return pd.DataFrame({'Regiao': ['Norte', 'Sul', 'Leste', 'Oeste'], 'Focos': [120, 45, 80, 200], 'Risco': ['Alto', 'Baixo', 'Medio', 'Critico']})
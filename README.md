# Hermes Reply – Fase 5 (Banco de Dados + ML básico)

Este repositório contém a entrega completa da **Fase 5** do desafio em parceria com a Hermes Reply:

- Modelagem relacional (DER + DDL Oracle)  
- Dataset simulado (7 dias, passo de 2 minutos, 6 máquinas)  
- ML básico (classificação NORMAL vs ANOMALO)  
- Documentação (README + roteiro de vídeo)  
- Estrutura de repositório pronta para publicação  

---

## Estrutura de pastas

hermes_reply_fase5/
data/
sensors_readings.csv
img/
der_official.png
confusion_matrix.png
roc_curve.png
feature_importance.png
notebooks/
hermes_reply_phase5_ml.ipynb
sql/
01_schema_oracle.sql
02_sample_queries.sql
src/
generate_data.py
docs/
video_script.md
README.md
requirements.txt
.gitignore

pgsql
Copiar código

---

## Diagrama ER

### Visão em Mermaid (renderizado pelo GitHub)

```mermaid
erDiagram
  PLANT ||--o{ LINE : has
  LINE ||--o{ MACHINE : has
  MACHINE ||--o{ SENSOR : has
  UNIT ||--o{ SENSOR_TYPE : defines
  SENSOR_TYPE ||--o{ SENSOR : categorizes
  SENSOR ||--o{ READING : produces
  SENSOR ||--o{ LABEL : may_have

  PLANT {
    int plant_id PK
    string name
  }
  LINE {
    int line_id PK
    int plant_id FK
    string name
  }
  MACHINE {
    int machine_id PK
    int line_id FK
    string name
  }
  UNIT {
    int unit_id PK
    string name
    string symbol
  }
  SENSOR_TYPE {
    int sensor_type_id PK
    string name
    float expected_min
    float expected_max
    int unit_id FK
  }
  SENSOR {
    int sensor_id PK
    int machine_id FK
    int sensor_type_id FK
    string serial
    datetime installed_at
  }
  READING {
    int reading_id PK
    int sensor_id FK
    datetime reading_time
    float value
  }
  LABEL {
    int label_id PK
    int sensor_id FK
    datetime reading_time
    string status
  }
DER oficial
A imagem oficial exportada está disponível em:
img/der_official.png

Como executar o notebook
Opção A – Google Colab (mais simples)
Abra notebooks/hermes_reply_phase5_ml.ipynb no Colab.

Faça upload do arquivo data/sensors_readings.csv.

Ajuste no código o caminho do CSV:

python
Copiar código
DATA_PATH = "sensors_readings.csv"
Crie a pasta de imagens (se não existir):

python
Copiar código
import os
os.makedirs("img", exist_ok=True)
IMG_DIR = "img"
Instale dependências:

python
Copiar código
!pip install pandas numpy scikit-learn matplotlib
Vá em Executar → Executar tudo.

Opção B – Local (venv)
Crie e ative um ambiente virtual.

Instale dependências:

bash
Copiar código
pip install -r requirements.txt
Abra o notebook no Jupyter/VSCode e execute todas as células.

Resultados do ML
As imagens geradas ficam em img/:

confusion_matrix.png – matriz de confusão do modelo final

roc_curve.png – curva ROC/AUC

feature_importance.png – se RandomForest for o melhor modelo

Limitações e próximos passos
Dados simulados (não medidos em planta real).

Regra de rótulo determinística (thresholds simples).

Em produção, recomenda-se: tuning, validação de domínio, monitoramento, e avaliação temporal (drift).

Vídeo 
👉 Assista aqui https://youtu.be/JzS-hqwBYyU

Versões usadas
Python 3.11+

pandas, numpy, scikit-learn, matplotlib

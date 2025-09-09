# Hermes Reply – Fase 5 (Banco de Dados + ML básico)

Este repositório contém uma solução completa e reprodutível para a entrega da Fase 5:
- **Modelagem relacional** (DER + DDL Oracle)
- **Dataset simulado** (7 dias, passo de 2 minutos, 6 máquinas)
- **ML básico** (classificação NORMAL vs ANOMALO)
- **Documentação** (README + roteiro de vídeo)
- **Estrutura de repositório** pronta para publicação

## Estrutura de pastas
```
hermes_reply_fase5/
  data/
    sensors_readings.csv
  img/
    der_placeholder_mermaid.png
    confusion_matrix.png
    roc_curve.png
    feature_importance.png       # gerado se RandomForest for o melhor
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
```

## Diagrama ER (referência rápida)
O diagrama oficial deve ser exportado pelo **Oracle SQL Developer Data Modeler** (passo a passo abaixo). Enquanto isso, segue uma visão Mermaid para referência:

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
    NUMBER plant_id PK
    VARCHAR name
  }
  LINE {
    NUMBER line_id PK
    NUMBER plant_id FK
    VARCHAR name
  }
  MACHINE {
    NUMBER machine_id PK
    NUMBER line_id FK
    VARCHAR name
  }
  UNIT {
    NUMBER unit_id PK
    VARCHAR name
    VARCHAR symbol
  }
  SENSOR_TYPE {
    NUMBER sensor_type_id PK
    VARCHAR name
    NUMBER expected_min
    NUMBER expected_max
    NUMBER unit_id FK
  }
  SENSOR {
    NUMBER sensor_id PK
    NUMBER machine_id FK
    NUMBER sensor_type_id FK
    VARCHAR serial UNIQUE
    TIMESTAMP installed_at
  }
  READING {
    NUMBER reading_id PK
    NUMBER sensor_id FK
    TIMESTAMP reading_time
    NUMBER value
  }
  LABEL {
    NUMBER label_id PK
    NUMBER sensor_id FK
    TIMESTAMP reading_time
    VARCHAR status
  }
```

> A imagem `img/der_placeholder_mermaid.png` é apenas um **placeholder**. Exporte o **DER oficial** como `img/der_official.png` seguindo o guia abaixo.

## Como exportar o DER oficial (Oracle SQL Developer Data Modeler)
1. Abra o **Oracle SQL Developer Data Modeler**.
2. **File > Import > DDL File…** e selecione `sql/01_schema_oracle.sql`.
3. Verifique entidades e relacionamentos, ajuste o layout se necessário.
4. **File > Export > To Image…** e salve como `img/der_official.png`.
5. (Opcional) Atualize este README para apontar para `der_official.png`.

## Como executar o notebook

### Opção A – Google Colab (mais simples)
1. Abra `notebooks/hermes_reply_phase5_ml.ipynb` no Colab.
2. Crie as pastas `img/` e `data/` caso não existam:
   ```python
   !mkdir -p img data
   ```
3. Faça upload de `data/sensors_readings.csv` para a pasta `data/` no Colab.
4. Instale dependências:
   ```python
   !pip install pandas numpy scikit-learn matplotlib
   ```
5. Execute **todas as células**. Os gráficos serão salvos em `img/`.

### Opção B – Local (venv)
1. Crie um ambiente virtual e ative-o.
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Abra o notebook no Jupyter/VSCode e execute todas as células.

## Resultados do ML
As imagens geradas ficam em `img/`:
- `confusion_matrix.png` – matriz de confusão do modelo final
- `roc_curve.png` – curva ROC/AUC
- `feature_importance.png` – se RandomForest for o melhor

## Limitações e próximos passos
- Dados **simulados** (não medidos em planta real).
- Regra de rótulo **determinística** (thresholds simples).
- Em produção, recomenda-se: tuning, validação de domínio, monitoramento, e avaliação temporal (drift).

## Vídeo (≤ 5 min)
Cole aqui o link do seu vídeo **Não listado** no YouTube:
- **Link:** _adicione aqui_

## Versões usadas
- Python 3.11+
- pandas, numpy, scikit-learn, matplotlib

Boa entrega! :)


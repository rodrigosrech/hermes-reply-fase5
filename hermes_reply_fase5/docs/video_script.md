# Roteiro de Vídeo (≤ 5 minutos)

**00:00–00:30 – Contexto**
- Objetivo: detectar anomalias operacionais (NORMAL vs ANOMALO) a partir de sensores.
- Pipeline: dados simulados ⇒ banco relacional ⇒ modelo de ML ⇒ métricas e gráficos.

**00:30–01:20 – DER**
- Mostre `img/der_official.png`. Comente entidades (plant, line, machine, sensor_type, unit, sensor, reading, label).
- Explique chaves, cardinalidades e índices (ex.: idx_reading_sensor_time).

**01:20–02:00 – Dados**
- `data/sensors_readings.csv`: 7 dias, passo de 2 minutos, 6 máquinas.
- Variáveis: temperatura, vibração, pressão, corrente + `label` (regra explícita).

**02:00–03:30 – ML**
- Notebook `notebooks/hermes_reply_phase5_ml.ipynb`.
- Baseline vs Logistic Regression vs RandomForest (escolha por acurácia).
- Mostre matriz de confusão e ROC. Comente trade-offs (precisão vs recall).

**03:30–04:30 – Execução**
- Mostre `README.md` (como rodar no Colab/local).
- Aponte as pastas (`data/`, `img/`, `sql/`, `src/`, `notebooks/`).

**04:30–05:00 – Encerramento**
- Limitações (dados simulados, thresholds simples).
- Próximos passos (tuning, validação de domínio, monitoramento).

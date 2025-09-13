# DatIQ Portfolio 🚀  

Este repositorio contiene un proyecto completo de *Business Intelligence* y *Agentes IA* aplicado a una empresa ficticia de piezas de desguace.  
El objetivo es demostrar un stack moderno de **Data Partner**: desde el almacenamiento de datos hasta la automatización de reportes con IA.  

---

## 📂 Estructura del proyecto
datIQ-portfolio/
│
├── data/ # Datasets ficticios en CSV
├── scripts/ # Scripts Python organizados por servicio
│ └── utils.py # Conexión a Supabase
├── notebooks/ # Notebooks de exploración y pruebas
├── dashboards/ # Dashboards exportados (Power BI / Looker Studio)
├── agents/ # Flujos de n8n y Flowise
├── .env.example # Plantilla de variables de entorno
├── requirements.txt # Dependencias de Python
└── README.md # Este archivo

---

## 🚀 Stack principal  

- **Base de datos:** PostgreSQL en Supabase  
- **Lenguaje:** Python (pandas, SQLAlchemy, Prophet, XGBoost)  
- **Visualización:** Power BI Service / Looker Studio  
- **Automatización:** n8n + Flowise (Agentes IA)  
- **Control de versiones:** GitHub  

---

## 🗂️ Servicios implementados  

1. **Limpieza y validación de datos**  
   - Detección de nulos, duplicados, inconsistencias, outliers.  
   - Corrección y carga de datos limpios en la base.  

2. **Dashboards con KPIs**  
   - Métricas clave de ventas, stock y clientes.  
   - Diseñados en Power BI y Looker Studio.  
   - Exportables en PDF.  

3. **Scraping de competencia**  
   - Extracción de precios en e-commerce similares.  
   - Comparación de precios y márgenes.  

4. **Predicción de demanda**  
   - Modelos Prophet (tendencias y estacionalidad).  
   - Modelos XGBoost (predicción más avanzada).  
   - Casos aplicados a ventas y rotación de stock.  

5. **Agentes IA y automatización**  
   - Reportes automáticos en PDF enviados a clientes.  
   - Chatbot para consultar ventas en lenguaje natural.  
   - Flujos creados en n8n y Flowise AI.  

---

# 🇨🇭 Swiss Living Cost Calculator PRO  
**A complete Swiss living-cost analysis tool built with Streamlit, Plotly, and real-time currency API.**  
Automatically calculates monthly living cost, visualizes spending structure, and exports results as a multi-page PDF.

<img width="1910" height="915" alt="image" src="https://github.com/user-attachments/assets/4477e004-95ff-479e-8797-ade9e38a03da" />


---

## 🔥 Overview  
This app helps users living in Switzerland estimate and visualize their monthly expenses.  
It includes real-time exchange rates, cost breakdown charts, and a fully automated PDF report generator.

---

## ✨ Features  

### ✔ 1. Real-Time Exchange Rates  
- Fetches CHF → EUR/USD/KRW currency data  
- Displays conversion for the total monthly cost  

### ✔ 2. Monthly Fixed Cost Input  
- Rent  
- Insurance  
- Transport  
- Internet/Mobile  
- Childcare  
- Bills  

### ✔ 3. Monthly Variable Cost Input  
- Food  
- Baby  
- Shopping  
- Health  
- Entertainment  

### ✔ 4. Automatic Summary  
- Total fixed + variable cost  
- Total monthly living cost (CHF)  
- Currency conversion summary  


### ✔ 5. Data Visualization  
- **Pie Chart** for spending structure  
- **Bar Chart** for category comparison  
- High-resolution Plotly images  
<img width="1912" height="924" alt="image" src="https://github.com/user-attachments/assets/1b13c503-3a74-4f2a-8b2f-291381241682" />

### ✔ 6. PDF Export (Multi-Page)  
- Page 1: Summary + Pie Chart  
- Page 2: Bar Chart  
- Unicode-safe Apple font  
- Ready for printing or sharing  
<img width="1911" height="916" alt="image" src="https://github.com/user-attachments/assets/664df1fc-93e1-4e9f-b644-4856a978ae08" />
---

## 🖥️ Demo (Streamlit Cloud)  
👉 https://sabinsim-swiss-living-app-swiss-living-app-fy0hql.streamlit.app/

---

## 📷 Screenshots  
> You can add them later after taking screenshots (recommend from Streamlit UI + PDF).

- Home / Input Page  
- Summary Page  
- Pie Chart  
- Bar Chart  
- PDF Example (2 pages)

---

## 🛠️ Tech Stack

### **Frontend / UI**
- Streamlit

### **Backend**
- Python 3.9+
- Real-time Exchange Rate API (open.er-api.com)

### **Visualization**
- Plotly Express  
- Kaleido (image export)

### **PDF Generation**
- FPDF2  
- AppleSDGothicNeo (Unicode font)

---

## 📁 Folder Structure  

```

📦 swiss_living_app/
├── swiss_living_app.py
├── requirements.txt
├── README.md
└── (Generated PDF files)

```

---

## ▶️ How to Run (Local)

1. Clone repo  
```

git clone [https://github.com/USERNAME/sw-living-calculator](https://github.com/USERNAME/sw-living-calculator)
cd sw-living-calculator

```

2. Install dependencies  
```

pip install -r requirements.txt

```

3. Run app  
```

streamlit run swiss_living_app.py

```

---

## 📄 requirements.txt  


```

streamlit
requests
plotly
kaleido
fpdf2

```

---

## ❤️ Author  
**Sabin Sim**  
Junior Developer in Switzerland  
Building practical tools for everyday life.


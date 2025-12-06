import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
from fpdf import FPDF
import tempfile

st.title("🇨🇭 Swiss Living Cost Calculator PRO")

# Initialize session state
if "fixed" not in st.session_state:
    st.session_state.fixed = {}

if "variable" not in st.session_state:
    st.session_state.variable = {}

# Fetch exchange rates
def get_rates():
    url = "https://open.er-api.com/v6/latest/CHF"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    rates = data["rates"]

    return {
        "EUR": rates["EUR"],
        "USD": rates["USD"],
        "KRW": rates["KRW"]
    }

# Categories
fixed_cost_categories = [
    "Rent",
    "Insurance",
    "Internet & Mobile",
    "Transport Pass",
    "Kindergarten/Childcare",
    "Bills"
]

variable_cost_categories = [
    "Food",
    "Baby",
    "Shopping",
    "Medicine/Health",
    "Entertainment"
]

menu = st.sidebar.radio("Menu", [
    "Fixed Costs",
    "Variable Costs",
    "Summary"
])

# ======================
# Fixed Costs
# ======================
if menu == "Fixed Costs":
    st.subheader("🏠 Monthly Fixed Costs")

    for cat in fixed_cost_categories:
        st.session_state.fixed[cat] = st.number_input(
            f"{cat} (CHF)", min_value=0.0, format="%.2f",
            key=f"fixed_{cat}"
        )

    st.write("Your fixed costs:", st.session_state.fixed)

# ======================
# Variable Costs
# ======================
elif menu == "Variable Costs":
    st.subheader("🛒 Monthly Variable Costs")

    for cat in variable_cost_categories:
        st.session_state.variable[cat] = st.number_input(
            f"{cat} (CHF)", min_value=0.0, format="%.2f",
            key=f"var_{cat}"
        )

    st.write("Your variable costs:", st.session_state.variable)

# ======================
# Summary
# ======================
elif menu == "Summary":
    st.subheader("📊 Monthly Summary")

    total_fixed = sum(st.session_state.fixed.values())
    total_variable = sum(st.session_state.variable.values())
    grand_total = total_fixed + total_variable

    st.write(f"**Total Fixed Costs:** {total_fixed:.2f} CHF")
    st.write(f"**Total Variable Costs:** {total_variable:.2f} CHF")
    st.write(f"### 💰 Total Monthly Living Cost: {grand_total:.2f} CHF")

    # Prepare chart data
    total_data = {}
    for k, v in st.session_state.fixed.items():
        if v > 0:
            total_data[k] = v

    for k, v in st.session_state.variable.items():
        if v > 0:
            total_data[k] = v

    if total_data:
        df_total = pd.DataFrame({
            "Category": list(total_data.keys()),
            "Amount": list(total_data.values())
        })

        st.write("### Spending Breakdown")
        st.dataframe(df_total)

        # PLOTLY graph_objects PIE CHART
        pie_colors = ["#66c2a5", "#fc8d62", "#8da0cb",
                      "#e78ac3", "#a6d854", "#ffd92f"]

        fig_pie = go.Figure(
            data=[go.Pie(
                labels=df_total["Category"],
                values=df_total["Amount"],
                marker=dict(colors=pie_colors)
            )]
        )

        st.write("### 📘 Pie Chart")
        st.plotly_chart(fig_pie, use_container_width=True)

        # PLOTLY graph_objects BAR CHART
        fig_bar = go.Figure(
            data=[go.Bar(
                x=df_total["Category"],
                y=df_total["Amount"],
                marker_color=pie_colors
            )]
        )

        st.write("### 📗 Bar Chart")
        st.plotly_chart(fig_bar, use_container_width=True)

    # Currency Conversion
    st.write("### 🌍 Currency Conversion")

    rates = get_rates()

    if rates:
        eur_value = grand_total * rates["EUR"]
        usd_value = grand_total * rates["USD"]
        krw_value = grand_total * rates["KRW"]

        st.write(f"**EUR:** € {eur_value:,.2f}")
        st.write(f"**USD:** $ {usd_value:,.2f}")
        st.write(f"**KRW:** ₩ {krw_value:,.0f}")
    else:
        st.warning("⚠ Unable to load exchange rate data.")


# ======================
# PDF EXPORT
# ======================

if st.button("📄 Download PDF Summary"):
    pdf = FPDF()
    pdf.add_page()

    # Universal Linux-safe font
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    pdf.cell(200, 10, txt="Swiss Living Cost Summary", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt=f"Total Fixed Costs: {total_fixed:.2f} CHF", ln=True)
    pdf.cell(200, 10, txt=f"Total Variable Costs: {total_variable:.2f} CHF", ln=True)
    pdf.cell(200, 10, txt=f"Total Monthly Living Cost: {grand_total:.2f} CHF", ln=True)
    pdf.ln(10)

    pdf.cell(200, 10, txt="Currency Conversion:", ln=True)
    pdf.cell(200, 10, txt=f"EUR: € {eur_value:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"USD: $ {usd_value:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"KRW: ₩ {krw_value:,.0f}", ln=True)

    # Export charts to images
    # Save Pie Chart
    pie_path = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name
    fig_pie.write_image(pie_path, scale=2)

    pdf.ln(10)
    pdf.image(pie_path, x=15, y=pdf.get_y(), w=170)

    # Page 2
    pdf.add_page()
    pdf.set_font("DejaVu", size=14)
    pdf.cell(200, 10, txt="Category – Bar Chart", ln=True)
    pdf.ln(5)

    bar_path = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name
    fig_bar.write_image(bar_path, scale=2)

    pdf.image(bar_path, x=15, y=pdf.get_y(), w=170)

    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_pdf.name)

    with open(temp_pdf.name, "rb") as f:
        st.download_button(
            label="📄 Download PDF",
            data=f,
            file_name="swiss_living_cost_summary.pdf",
            mime="application/pdf"
        )


if __name__ == "__main__":
    print(get_rates())


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Visualisasi data python")

upload_file = st.file_uploader("Masukan file csv", type=["csv"])

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)
    
    num_cols = df.select_dtypes(include=["number"]).columns
    
    op_visualisasi = st.selectbox("Jenis Visualisasi", ["Histogram", "Scatter Plot", "Line Chart"])
    
    btn_vis = st.button("Buat Visualisasi")

    if btn_vis:
        
        if op_visualisasi == "Histogram":
            selected_col = st.selectbox("Kolom untuk Histogram:", num_cols)

            fig, ax = plt.subplots()
            ax.hist(df[selected_col])
            ax.set_title(f"Histogram dari {selected_col}")
            ax.set_xlabel(selected_col)
            ax.set_ylabel("Frekuensi")
            st.pyplot(fig)

        elif op_visualisasi == "Scatter Plot":
            colomn_x = st.selectbox("Sumbu X:", num_cols)
            colomn_y = st.selectbox("Sumbu Y:", num_cols)

            fig, ax = plt.subplots()
            sns.scatterplot(x=df[colomn_x], y=df[colomn_y], ax=ax)
            st.pyplot(fig)

        elif op_visualisasi == "Line Chart":
            line_col = st.selectbox("Pilih kolom untuk Line Chart:", num_cols)

            st.line_chart(df[line_col])
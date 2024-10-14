import streamlit as st
import pandas as pd

# Загрузка данных
@st.cache_data
def load_data():
    df = pd.read_excel('KAZ_2017_FIES_v01_EN_M_v01_A_OCS.xlsx')
    return df

data = load_data()

# Заголовок
st.title('Динамика развития стран')

# Проверка структуры данных
st.write("Структура данных:")
st.dataframe(data.head())

# Выбор страны
countries = data['country'].unique()  # Предполагается, что есть колонка 'country'
country = st.selectbox('Выберите страну:', countries)

# Фильтрация данных
country_data = data[data['country'] == country]

# Визуализация
st.line_chart(country_data.set_index('year')['indicator'])  # Предполагается, что есть колонки 'year' и 'indicator'

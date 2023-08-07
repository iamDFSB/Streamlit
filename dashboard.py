import streamlit as st
import pandas as pd
import re
# Titulo
st.header('Meu primeiro DashBoard')

# Paragrafo ( O sidebar é para colocar ele na barra de perquisa na lateral)
st.sidebar.header('Nav Bar')
st.sidebar.text('Seleção dos Dados')

#  Pode colocar o texto em markdown utilizando sua linguagem
st.markdown('# *Texto teste*')

# Printando dados

dicio = {'nome':('Daniel','Renato','Luciana','Ana'),
         'idade':(23,34,27,53),}

df = pd.DataFrame({
    'nome':('Daniel','Renato','Luciana','Ana'),
    'idade':(23,34,27,53),
    'peso':(75.8,23.5,90.3,120.4),
})


check = st.sidebar.checkbox('Aceito os Termos')
slider = st.slider('Range',max_value=10)
radio = st.radio('Radio',('Parametro1','Parametro2','Parametro3'))

seletor = st.sidebar.selectbox('Seletores',('Gráfico','Tabela'))
seletor_mult = st.sidebar.multiselect('Mult seletores',('Gráfico','Tabela','Mapa','Seletor'))

data = st.date_input('Calendario')
if slider > 5:
    st.write('Maior que 5')


if check:
    st.sidebar.write('Aceitou')

    button_dicio = st.sidebar.button('Dicionário')
    button_tabela1 = st.sidebar.button('Tabela1')
    button_tabela2 = st.sidebar.button('Tabela2')
    button_tabela3 = st.sidebar.button('Tabela3')
    button_chart1 = st.sidebar.button('Gráfico de linha')
    button_chart2 = st.sidebar.button('Gráfico de Barra')



    lista_button = [button_tabela1, button_tabela2, button_tabela3, button_dicio, button_chart1, button_chart2]

    def escolha(lista):
        match lista:
            case [True, *_]:
                st.write('# Primeira Tabela com write()')
                st.write('# Tabela', df)

            case [False, True,*_]:
                st.sidebar.write('# Tabela usando table()')
                st.sidebar.table(df)

            case [False,False,True,*_]:
                st.write('# Tabela usando o dataframe()')
                st.dataframe(df)
                st.caption('Uma tabela de Exemplo')

            case [False,False,False,True,*_]:
                st.write('# Dados',dicio)

            case [False,False,False,False,True,*_]:
                st.write('Grafico de linha:')
                st.line_chart(df)

            case [False,False,False,False,False,True]:
                st.write('Grafico de barra:')
                st.bar_chart(df)


    escolha(lista_button)




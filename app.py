import streamlit as st
import re

def evaluate_expression(expression):
    # permitir apenas números, operadores e parênteses
    if re.match(r'^[0-9+\-*/(). ]+$', expression):
        try:
            # Executa a expressão
            result = eval(expression)
            return result
        except Exception as e:
            return f"Erro: {str(e)}"
    else:
        return "erro"

# Streamlit App
st.title("Avaliador de Expressões Matemáticas")

# Entrada do usuário
expression = st.text_input("Insira uma Expressão Matemática", "")

# Avalia e exibe o resultado
if expression:
    result = evaluate_expression(expression)
    if (result != "erro"):
        st.write(f"Resultado: {result}")
    else: 
        st.write("Entrada Inválida: Apenas números e operadores matemáticos são permitidos.")

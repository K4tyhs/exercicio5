import streamlit as st

st.title("Cardapio Lanchonete:")
st.write("Escolha seu lanche:")
st.write("Cachorro quente - 101")
st.write("Bauru simples - 102")
st.write("Hamburguer - 104")
st.write("Cheeseburguer - 105")
st.write("Refrigerante - 106")
st.sidebar.header("Me informe algumas coisas:")

while True:
    codigo = st.sidebar.number_input("Digite qual o codigo do seu pedido: ", max_value=106, min_value=101, step=1)
    quant = st.sidebar.number_input("Quantos desse item você deseja? ")
    st.write("Clique em calcular para ver o valor total do seu pedido")


    while True:
      compras = 0
      if st.button("calcular_bottom"):
          if codigo == 101:
                        compras = quant * 8.50
                        st.write(f"O valor da sua compra é: {compras}")
          elif codigo == 102:
                        compras = quant * 4.50
                        st.write(f"O valor da sua compra é: {compras}")
            
          elif codigo == 104:
                        compras = quant * 5.50
                        st.write(f"O valor da sua compra é: {compras}")
            
          elif codigo == 105:
                        compras = quant * 6.60
                        st.write(f"O valor da sua compra é: {compras}")
            
          elif codigo == 106:
                        compras = quant * 6.0
                        st.write(f"O valor da sua compra é: {compras}")
       
            
  

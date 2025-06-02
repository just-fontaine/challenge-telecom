import matplotlib.pyplot as plt

def plot_categoria(df, coluna):
    AZUL1, AZUL3, AZUL5 = '#174A7E', "#6495ED", '#94AFC5'
    VERMELHO1, VERDE1, CINZA3 = '#C3514E', '#0C8040', '#555655'
    cores = [AZUL1, AZUL3, AZUL5, VERMELHO1, VERDE1, CINZA3]  # Até 6 categorias diferentes

    # Contagem e preparação dos dados
    contagem = df[coluna].value_counts()
    df_plot = contagem.reset_index()
    df_plot.columns = [coluna, 'Quantidade']
    df_plot['Porcentagem'] = (df_plot['Quantidade'] / df_plot['Quantidade'].sum() * 100).round(2)

    # Gráfico de barras
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.bar(df_plot[coluna], df_plot['Quantidade'], color=cores[:len(df_plot)])
    plt.title(f'Distribuição de {coluna}', fontsize=14)
    plt.xlabel(coluna)
    plt.ylabel('Quantidade')

    # Gráfico de pizza
    plt.subplot(1, 2, 2)
    plt.pie(df_plot['Quantidade'],
            labels=df_plot[coluna],
            autopct='%1.1f%%',
            startangle=90,
            colors=cores[:len(df_plot)],
            textprops={'color': '#231F20'})  # cor do texto no gráfico (CINZA1)
    plt.title(f'{coluna} (Porcentagem)', fontsize=14)
    plt.axis('equal')

    plt.tight_layout()
    plt.show()

from flask import Flask, render_template_string
import random
import datetime

app = Flask(__name__)

# O conteúdo HTML e CSS embutido para o dashboard
HTML_CONTENT_DASHBOARD = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Vendas de Produtos</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #e9ecef;
            color: #343a40;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        header {
            background-color: #007bff;
            color: white;
            padding: 20px 30px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        header h1 {
            margin: 0;
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
        }
        .dashboard-container {
            flex-grow: 1;
            padding: 30px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            align-content: start;
        }
        .card {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            padding: 25px;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        }
        .card h2 {
            color: #007bff;
            margin-top: 0;
            margin-bottom: 15px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: 1.5em;
        }
        .card .value {
            font-size: 2.8em;
            font-weight: 700;
            color: #28a745; /* Verde para valores positivos */
            margin-bottom: 10px;
        }
        .card .description {
            font-size: 0.95em;
            color: #6c757d;
        }
        .card.red .value {
            color: #dc3545; /* Vermelho para atenção/queda */
        }
        .card.blue .value {
            color: #007bff; /* Azul para informação */
        }
        .product-list {
            list-style: none;
            padding: 0;
            text-align: left;
            margin-top: 20px;
        }
        .product-list li {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .product-list li:last-child {
            border-bottom: none;
        }
        .product-list .product-name {
            font-weight: 500;
        }
        .product-list .product-sales {
            font-weight: 700;
            color: #007bff;
        }
        footer {
            background-color: #343a40;
            color: white;
            text-align: center;
            padding: 15px;
            margin-top: auto;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <header>
        <h1>Dashboard de Vendas de Produtos</h1>
        <span>Última Atualização: {{ current_time }}</span>
    </header>

    <main class="dashboard-container">
        <div class="card">
            <h2>Vendas Totais Hoje</h2>
            <div class="value">${{ total_sales_today }}</div>
            <p class="description">Receita bruta gerada no dia.</p>
        </div>

        <div class="card blue">
            <h2>Produtos Vendidos</h2>
            <div class="value">{{ products_sold_today }}</div>
            <p class="description">Quantidade de itens únicos vendidos.</p>
        </div>

        <div class="card red">
            <h2>Ticket Médio</h2>
            <div class="value">${{ average_ticket }}</div>
            <p class="description">Valor médio por transação.</p>
        </div>

        <div class="card">
            <h2>Vendas por Produto</h2>
            <ul class="product-list">
                {% for product, sales in top_products %}
                <li>
                    <span class="product-name">{{ product }}</span>
                    <span class="product-sales">{{ sales }} unidades</span>
                </li>
                {% endfor %}
            </ul>
        </div>

        <div class="card blue">
            <h2>Clientes Ativos</h2>
            <div class="value">{{ active_customers }}</div>
            <p class="description">Clientes que fizeram compras hoje.</p>
        </div>

        <div class="card">
            <h2>Taxa de Conversão</h2>
            <div class="value">{{ conversion_rate }}%</div>
            <p class="description">Visitantes que se tornaram compradores.</p>
        </div>

    </main>

    <footer>
        <p>&copy; {{ current_year }} Dashboard de Vendas. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def dashboard():
    """
    Gera dados aleatórios para o dashboard e renderiza a página HTML.
    """
    # Gerar dados aleatórios para o dashboard
    total_sales = round(random.uniform(5000, 25000), 2)
    products_sold = random.randint(100, 500)
    num_transactions = random.randint(50, 200)
    average_ticket_value = round(total_sales / num_transactions if num_transactions > 0 else 0, 2)
    active_customers_count = random.randint(30, 150)
    conversion = round(random.uniform(1.5, 5.0), 2)

    # Top 3 produtos (aleatórios)
    products = ["Notebook Pro", "Smartphone X", "Fones de Ouvido BT", "Smartwatch Ultra", "Câmera Digital"]
    random.shuffle(products)
    top_products_data = [
        (products[0], random.randint(50, 150)),
        (products[1], random.randint(30, 100)),
        (products[2], random.randint(10, 70))
    ]

    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    current_year = datetime.datetime.now().year

    # Passa os dados para o template HTML
    return render_template_string(
        HTML_CONTENT_DASHBOARD,
        current_time=current_time,
        current_year=current_year,
        total_sales_today=f"{total_sales:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), # Formata para BR
        products_sold_today=products_sold,
        average_ticket=f"{average_ticket_value:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), # Formata para BR
        active_customers=active_customers_count,
        conversion_rate=conversion,
        top_products=top_products_data
    )

if __name__ == '__main__':
    app.run(debug=True)
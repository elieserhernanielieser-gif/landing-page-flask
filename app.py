from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    # Simulando dados que no futuro viriam de uma Base de Dados ou API externa
    featured_games = [
        {
            "id": 1,
            "league": "Liga dos Campeões",
            "time": "68'",
            "is_live": True,
            "home_team": "Real Madrid",
            "away_team": "Manchester City",
            "home_score": 2,
            "away_score": 1,
            "odds": {"1": "1.85", "X": "3.50", "2": "4.10"}
        },
        {
            "id": 2,
            "league": "Premier League",
            "time": "42'",
            "is_live": True,
            "home_team": "Arsenal",
            "away_team": "Liverpool",
            "home_score": 0,
            "away_score": 0,
            "odds": {"1": "2.40", "X": "3.10", "2": "2.90"}
        },
        {
            "id": 3,
            "league": "Girabola",
            "time": "18:00",
            "is_live": False,
            "home_team": "Petro de Luanda",
            "away_team": "1º de Agosto",
            "home_score": "-",
            "away_score": "-",
            "odds": {"1": "1.95", "X": "3.00", "2": "3.80"}
        }
    ]

    # Lista de diferenciais da plataforma (Features)
    platform_features = [
        {
            "title": "Levantamentos Instantâneos",
            "desc": "Receba os seus ganhos em menos de 2 minutos via Multicaixa Express ou transferência bancária direta.",
            "icon_d": "M13 10V3L4 14h7v7l9-11h-7z"  # Ícone de raio
        },
        {
            "title": "Super Odds Diárias",
            "desc": "Cotações aumentadas e margem reduzida nos jogos e campeonatos mais importantes da semana.",
            "icon_d": "M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"  # Ícone de tendência
        },
        {
            "title": "Cashout Total e Parcial",
            "desc": "Garanta o seu lucro ou reduza potenciais perdas a qualquer momento antes do apito final.",
            "icon_d": "M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"  # Ícone de verificação / segurança
        }
    ]
    # Lista de indicadores e estatísticas da plataforma
    platform_stats = [
        {"value": "+250K", "label": "Apostadores Ativos"},
        {"value": "< 2 min", "label": "Tempo Médio de Saque"},
        {"value": "98.2%", "label": "Payout do Mercado"},
        {"value": "24/7", "label": "Apoio ao Cliente"}
    ]

    return render_template(
        "index.html", 
        games=featured_games, 
        features=platform_features,
        stats=platform_stats
    )
    

if __name__ == "__main__":
    app.run(debug=True)
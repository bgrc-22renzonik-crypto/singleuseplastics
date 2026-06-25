from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Single Use Plastics</title>

<style>
body{
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 30px;
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    color: white;
}

.container{
    max-width: 1000px;
    margin: auto;
}

h1{
    text-align: center;
    font-size: 3rem;
    margin-bottom: 30px;
}

.card{
    background: rgba(255,255,255,0.08);
    padding: 25px;
    margin-bottom: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    transition: transform 0.3s ease;
}

.card:hover{
    transform: translateY(-5px);
}

h2{
    color: #7dd3fc;
}

p{
    font-size: 18px;
    line-height: 1.8;
}

.footer{
    text-align: center;
    margin-top: 40px;
    color: #cbd5e1;
}
</style>
</head>

<body>

<div class="container">

<h1>🌍 Single Use Plastics</h1>

<div class="card">
    <h2>📚 What Are Single Use Plastics?</h2>
    <p>
        Single-use plastics are items that are used once and then thrown away.
        Examples include plastic straws, shopping bags, water bottles and food packaging.
    </p>
</div>

<div class="card">
    <h2>🐢 Environmental Effects</h2>
    <p>
        Plastic waste can pollute oceans, rivers and land. Animals can mistake plastic
        for food, which may harm them. Over time, plastic breaks into tiny pieces called
        microplastics that spread through the environment.
    </p>
</div>

<div class="card">
    <h2>♻️ How Can We Help?</h2>
    <p>
        We can reduce plastic waste by using reusable bags, reusable bottles and
        recycling correctly. Small actions can make a big difference.
    </p>
</div>

<div class="card">
    <h2>💡 Conclusion</h2>
    <p>
        Single-use plastics are a major environmental problem, but everyone can help.
        By making simple choices every day, we can reduce waste and protect our planet.
    </p>
</div>

<div class="footer">
    Created for Year 7–8 Students 🌎
</div>

</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

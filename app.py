from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Single Use Plastics</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e3a8a);
            color: white;
            margin: 0;
            padding: 30px;
        }

        h1 {
            text-align: center;
            font-size: 3rem;
            margin-bottom: 30px;
        }

        .card {
            background: rgba(255,255,255,0.08);
            padding: 25px;
            margin-bottom: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            transition: transform 0.3s;
        }

        .card:hover {
            transform: translateY(-4px);
        }

        h2 {
            color: #7dd3fc;
        }

        p {
            line-height: 1.8;
            font-size: 18px;
        }

        .footer {
            text-align: center;
            margin-top: 30px;
            color: #cbd5e1;
        }
    </style>
</head>
<body>

<h1>🌍 Single Use Plastics</h1>

<div class="card">
    <h2>📚 What Are Single Use Plastics?</h2>
    <p>
        Single use plastics are plastic items that are only used once before being
        thrown away. Examples include plastic straws, shopping bags, water bottles,
        and food packaging.
    </p>
</div>

<div class="card">
    <h2>🐢 Environmental Effects</h2>
    <p>
        Single use plastics can pollute oceans, rivers, and land. Animals may
        mistake plastic for food, which can harm them. Over time, plastics break
        into tiny pieces called microplastics that can spread through ecosystems.
    </p>
</div>

<div class="card">
    <h2>♻️ How Can We Help?</h2>
    <p>
        People can reduce plastic waste by using reusable bags, reusable water
        bottles, and recycling correctly. Small changes can make a big difference.
    </p>
</div>

<div class="card">
    <h2>💡 Conclusion</h2>
    <p>
        Single use plastics are a major environmental issue, but everyone can help
        reduce the problem through simple everyday actions.
    </p>
</div>

<div class="footer">
    Created for Year 7–8 Students 🌎
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

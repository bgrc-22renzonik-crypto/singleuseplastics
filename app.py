# app.py

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Single Use Plastics</title>

<style>
body{
    font-family: Arial, sans-serif;
    margin:0;
    padding:30px;
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    color:white;
}

h1{
    text-align:center;
    font-size:3rem;
}

.card{
    background:rgba(255,255,255,0.08);
    padding:20px;
    margin:20px 0;
    border-radius:15px;
    box-shadow:0 4px 8px rgba(0,0,0,0.3);
}

h2{
    color:#7dd3fc;
}

p{
    line-height:1.8;
    font-size:18px;
}

.footer{
    text-align:center;
    margin-top:30px;
    color:#cbd5e1;
}
</style>

</head>
<body>

<h1>🌍 Single Use Plastics</h1>

<div class="card">
<h2>📚 What Are Single Use Plastics?</h2>
<p>
Single use plastics are plastic items that are used once and then thrown away.
Examples include plastic straws, shopping bags, water bottles and food packaging.
</p>
</div>

<div class="card">
<h2>🐢 Environmental Effects</h2>
<p>
Plastic waste can pollute oceans, rivers and land. Animals may mistake plastic
for food, which can cause harm. Plastic can also break into tiny pieces called
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
Single use plastics are a major environmental issue, but everyone can help by
making better choices every day.
</p>
</div>

<div class="footer">
Created for Year 7–8 Students 🌎
</div>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Website created successfully! Open index.html in your browser.")

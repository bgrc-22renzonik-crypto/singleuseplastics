import streamlit as st

st.set_page_config(
    page_title="Single Use Plastics",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #003366, #0066cc, #3399ff);
}

h1 {
    color: white !important;
    text-align: center;
    font-size: 4rem !important;
}

.card {
    background: rgba(255,255,255,0.15);
    padding: 35px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

.card h2 {
    color: #e0f2fe;
    font-size: 2.3rem;
}

.card p {
    color: white;
    font-size: 30px;
    line-height: 2.2;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1>🌍 Single-Use Plastics 🌍</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">
<h2>📚 What Are Single-Use Plastics?</h2>
<p>
Single-use plastics are items made from plastic that are designed to be used only once before they are thrown away.
Examples include shopping bags, plastic straws, water bottles, food wrappers and disposable cutlery. These items are
very common because they are cheap, lightweight and easy to use. However, because millions of people use them every day,
a huge amount of plastic waste is created around the world. Much of this waste ends up in landfill sites, rivers,
beaches and oceans. Unlike materials such as paper, plastic takes a very long time to break down naturally. Some types
of plastic can remain in the environment for hundreds of years. As more plastic products are produced and used, the
amount of waste continues to grow. This is why single-use plastics have become a major environmental issue in many
countries around the world.
</p>
</div>

<div class="card">
<h2>🐢 Environmental Effects</h2>
<p>
Plastic pollution has a serious impact on the environment. When plastic is dropped on the ground or not recycled
properly, it can be carried by wind and rain into rivers, lakes and oceans. Many animals accidentally eat plastic
because they mistake it for food. Sea turtles, fish, seabirds and other wildlife can be harmed by plastic pollution.
Animals may become sick, injured or even die after swallowing plastic waste. Plastic can also become tangled around
animals, making it difficult for them to move or survive. Over time, larger pieces of plastic break down into tiny
pieces called microplastics. These small pieces can spread through the environment and are extremely difficult to
remove. Scientists have discovered microplastics in oceans, rivers, soil and even some food products, showing how
widespread the problem has become.
</p>
</div>

<div class="card">
<h2>♻️ How Can We Help?</h2>
<p>
Although plastic pollution is a major problem, there are many simple things people can do to help. One of the easiest
ways is to use reusable products instead of disposable ones. For example, people can carry reusable shopping bags,
reusable water bottles and reusable lunch containers. Recycling correctly can also help reduce the amount of waste
that ends up in landfill sites. Schools, families and local communities can organise clean-up events to remove litter
from parks, beaches and public spaces. Businesses and governments can also help by reducing unnecessary plastic
packaging and encouraging environmentally friendly alternatives. While one person's actions may seem small, many small
actions combined can make a very big difference.
</p>
</div>

<div class="card">
<h2>💡 Conclusion</h2>
<p>
In conclusion, single-use plastics are useful products that many people rely on every day, but they also create major
environmental problems. Plastic waste can pollute natural environments, harm wildlife and contribute to long-term
pollution around the world. Because plastic takes such a long time to break down, its effects can last for many years.
Fortunately, there are many ways people can help reduce the problem. By using reusable products, recycling responsibly
and making environmentally friendly choices, individuals can contribute to a cleaner future. If more people work
together to reduce plastic waste, it will help protect the environment and create a healthier world for future
generations.
</p>
</div>
""", unsafe_allow_html=True)

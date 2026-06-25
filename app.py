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
    color: white;
    text-align: center;
    font-size: 4rem;
}

.card {
    background: rgba(255,255,255,0.15);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

h2 {
    color: #e0f2fe;
    font-size: 2.2rem;
}

p {
    color: white;
    font-size: 26px;
    line-height: 2;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 Single-Use Plastics")

st.markdown("""
<div class="card">
<h2>📚 What Are Single-Use Plastics?</h2>
<p>
Single-use plastics are things made of plastic that we only use once before
throwing them away. Some examples are plastic straws, shopping bags, water
bottles and food wrappers. These items can be useful and convenient, but because
millions of people use them every day, they create a huge amount of rubbish.
Most of this rubbish takes a very long time to break down, which means it can
stay in the environment for many years.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>🐢 Environmental Effects</h2>
<p>
Plastic pollution is a serious problem for our planet. When plastic is dropped
on the ground or not recycled properly, it can end up in rivers, beaches and
oceans. Animals sometimes mistake plastic for food, which can make them sick or
even cause them to die. Over time, plastic can break into tiny pieces called
microplastics. These small pieces can spread through the environment and are
very difficult to remove.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>♻️ How Can We Help?</h2>
<p>
There are many simple ways we can help reduce plastic waste. We can bring a
reusable water bottle, use reusable shopping bags and recycle correctly. Schools,
families and communities can all work together to reduce the amount of plastic
that is thrown away. Even small changes can make a positive difference when lots
of people take part.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>💡 Conclusion</h2>
<p>
To conclude, single-use plastics are causing problems for the environment, but
there are ways we can help. By making better choices every day and reducing the
amount of plastic we use, we can help keep our planet cleaner and safer for
animals and future generations. Everyone can play a part in protecting the
environment.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "<h3 style='text-align:center; color:white;'>🌎 Created for Year 7–8 Students 🌎</h3>",
    unsafe_allow_html=True
)
